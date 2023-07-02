from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from .models import Profile
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError
from .utils import send_email_verify

User = get_user_model()

class MyAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
            if  not self.user_cache.email_verify:
                send_email_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Ваша почта не потверждена. Письмо отправлено',
                    code='invalid_login',
                )
        return self.cleaned_data

class UserCreateOurReg(UserCreationForm):

    email = forms.EmailField(required=True, label=('Ваша почта'))
    phone = PhoneNumberField(region='RU', widget=forms.TextInput(attrs={'placeholder': _('+7(999)123-45-67')}), label=_("Номер телфона"), required=False)

    class Meta:
        model = User
        fields = ['email','phone', 'password1', 'password2']

class UserEditUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(region='RU', widget=forms.TextInput(attrs={'placeholder': _('+7(999)123-45-67')}), label=_("Номер телфона"), required=False)
    adress = forms.CharField(label=('Ваш адресс'))
    org = forms.CharField(label=('Ваша организация'), max_length=100)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','phone','adress','org']

class ImgUserEditUpdateForm(forms.ModelForm):
    img = forms.ImageField(label=('Фотография профиля'))

    class Meta:
        model = Profile
        fields = ['img' ]