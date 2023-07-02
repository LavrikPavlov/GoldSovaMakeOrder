from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout

from django.views import View
from django.utils.http import urlsafe_base64_decode
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator as token_generator


from .forms import MyAuthenticationForm, UserCreateOurReg, ImgUserEditUpdateForm, UserEditUpdateForm
from order.models import MakeOrder
from .utils import send_email_verify, login_excluded

User = get_user_model()


class MyLoginView(LoginView):
    form_class = MyAuthenticationForm
    
class MyLogoutView(LogoutView):
    def logout_site(request):
        logout(request)
        return redirect('auth')


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            email = request.user.email
            messages.success(request, f'Успешная потверждение почты: {email}')
            return redirect('profile')
        messages.warning(request, f'Ошибка в потверждении почты')
        return redirect('home')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


@login_required
def profile(request):
    history = MakeOrder.objects.filter(email_id = request.user.id)
    return render(request, 'users/profile.html', 
                  {
                    'title': 'Профиль',
                    'history': history,
                  })

@login_required
def edit(request):
    try:
        if request.method == "POST":
            img_profile = ImgUserEditUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            update_user = UserEditUpdateForm(request.POST, instance=request.user)
            if update_user.is_valid() and img_profile.is_valid():
                update_user.save()
                img_profile.save()
                email = update_user.cleaned_data.get('email')
                messages.success(request, f'Успешная обновление данных пользователя {email}')
                return redirect('profile')
        else:
            img_profile = ImgUserEditUpdateForm(instance=request.user.profile)
            update_user = UserEditUpdateForm(instance=request.user)
            data ={
            'img_profile': img_profile,
            'update_user': update_user,
            'title': 'Обновление профиля'
            }
        return render(request, 'users/edit.html', data)
    except Exception:
        messages.warning('profile')
        return redirect('profile')

@login_excluded('profile')
def register(request):
    if request.method == "POST":
        form = UserCreateOurReg(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_verify(request, user)
            messages.success(request, f'Сообщение для потверждение было отправлено вам на: {email}')
            return redirect('confirm_email')
    else:
        form = UserCreateOurReg()

    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация'})

