from . import views
from django.urls import path

app_name = 'order'

urlpatterns = [
   path('', views.order_conditions, name='order'),
   path('make_order',views.make_order, name='make_order_form'),
   path('download', views.download_file, name='download_file'),
   path('delete_order/<int:number_order>', views.delete_order, name='delete_order')
]