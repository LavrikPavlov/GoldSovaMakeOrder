from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as authViews

from .views import EmailVerify


urlpatterns = [
   path('',views.register, name='reg'),
   path('confirm_email/', TemplateView.as_view(template_name = 'users/confirm_email.html'), name='confirm_email'),
   path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
   path('respassword/',authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'), name='pass_reset'),
   path('password_reset_confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name='password_reset_confirm'),
   path('password_reset/done/',
         authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name='password_reset_done'),
   path('password_reset_complete/',
         authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name='password_reset_complete'),
]