from django.db import models
from users.models import User
from .utils import user_directory_path 
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class MakeOrder(models.Model):

    STATUS = [
        (1, 'Рассмотрение'),
        (2, 'Начато'),
        (3, 'Потвержден'),
        (4, 'Выполнение'),
        (5, 'Выполнен')
    ]

    number_order = models.AutoField('Номер заказа', primary_key = True)
    email = models.ForeignKey(User, on_delete= models.CASCADE)
    file_order = models.FileField('Накладная', upload_to=user_directory_path)
    status_order = models.PositiveSmallIntegerField('Статус заказа', default = 1, choices = STATUS)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    uploaded = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ: №{self.number_order}"
    

@receiver(pre_delete, sender=MakeOrder)
def mymodel_delete(sender, instance, **kwargs):
    instance.file_order.delete(False)

