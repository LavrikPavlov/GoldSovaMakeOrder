import os
import mimetypes

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import MakeOrderForm, DeleteOrderForm
from .utils import work_with_excel
from .models import MakeOrder


@login_required
def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Заявка.xlsx'
    filepath = BASE_DIR + '/files/' + filename
    work_with_excel(filepath, request.user.adress)
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = 'attachment; filename=Zayvka.xlsx'
    return response

@login_required
def make_order(request):
    if request.user.succes_user:
        if request.method == "POST":
            ordermake = MakeOrderForm(request.POST, request.FILES)
            org = request.user.org
            adress = request.user.adress
            if ordermake.is_valid():
                instance = ordermake.save(commit=False)
                instance.email_id = request.user.id
                instance.save()
                email = request.user.org
                messages.success(request, f'Заявка {email} отправлена ')
                return redirect('profile')
        else:
            ordermake = MakeOrderForm()
            org = request.user.org
            adress = request.user.adress
        return render(request, 'order/make_order.html', 
                      {
                        'org': org,
                        'adress': adress,
                        'form': ordermake,
                        'title':'Форма отправки заявки'
                      })
    else:
        messages.warning(request, f'У вас не достаточно прав')
        return redirect('profile')

@login_required
def order_conditions(request):
    if request.user.succes_user:
        return render(request, 'order/order.html', 
                      {
                        'title':'Условия оформления заявки'
                      })
    else:
        messages.warning(request, f'У вас не достаточно прав')
        return redirect('profile')


@login_required   
def delete_order(request, number_order):
    order = MakeOrder.objects.get(number_order=number_order)
    if request.user.id == order.email_id:
        messages.success(request, f'Ваш заказ №{order.number_order} удален')
        order.delete()
        return redirect('profile')
    else:
        messages.success(request, f'Не ваш заказ')
        return redirect('profile')
    
    