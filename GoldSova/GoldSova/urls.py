from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import MyLoginView, MyLogoutView
from users import views as UsersViews



urlpatterns = [
    path('admin_work_with_site/', admin.site.urls, name = 'admin_action'),
    path('',include('main.urls')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('reg/', include('users.urls')),
    path('order/', include('order.urls')),
    path('login/', MyLoginView.as_view(template_name='users/user.html',redirect_authenticated_user=True), name='auth'),
    path('profile/', UsersViews.profile, name='profile'),
    path('edit/', UsersViews.edit, name='edit'),
    path('logout/',MyLogoutView.logout_site, name='exit'),
] 

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)