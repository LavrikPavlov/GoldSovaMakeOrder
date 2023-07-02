
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Volume, PhotosProduct




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'catalog/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'title': 'Каталог'
                  })

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    volume = get_object_or_404(Volume, name_id = id)
    photo = get_object_or_404(PhotosProduct, name_id = id)
    
    return render(request, 'catalog/product/detail.html', 
                  {
                   'product': product, 
                   'volume':volume, 
                   'photo': photo, 
                   'title': 'О продукте'
                  })


