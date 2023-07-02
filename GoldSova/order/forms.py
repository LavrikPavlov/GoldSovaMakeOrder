from django import forms
from .models import MakeOrder


class MakeOrderForm(forms.ModelForm):
    file_order = forms.FileField(label=('Загрузить заказ'))

    class Meta:
        model = MakeOrder
        fields = ['file_order',]

class DeleteOrderForm(forms.ModelForm):
    number_order = forms.IntegerField(label=('Введите номер заказа:'))

    class Meta:
        model = MakeOrder
        fields = ['number_order',]