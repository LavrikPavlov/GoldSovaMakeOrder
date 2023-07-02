from django.db import models
from django.contrib.auth.models import User,AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from PIL import Image

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('Почта должна быть'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('email_verify', True)
        extra_fields.setdefault('succes_user', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    succes_user = models.BooleanField('Потверждение пользователя', default=False,)
    email_verify = models.BooleanField('Потверждение почты', default=False,)
    phone = PhoneNumberField(region='RU')
    adress = models.CharField('Адресс', default='',max_length=250)
    org = models.TextField('Организация', default='',max_length=100)

    objects = CustomUserManager()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='dafault.jpg', upload_to='user_images')
   
    def __str__(self):
        return f'Пользователь: {self.user.email}'
    

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователе'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

@receiver(pre_delete, sender=Profile)
def mymodel_delete(sender, instance, **kwargs):
    instance.img.delete(False)