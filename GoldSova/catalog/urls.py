from . import views
from django.urls import path

app_name = 'catalog'

urlpatterns = [
   path('', views.product_list, name='product_list'),
   path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
   path('<int:id>/<slug:slug>', views.product_detail, name='product_detail')
]

