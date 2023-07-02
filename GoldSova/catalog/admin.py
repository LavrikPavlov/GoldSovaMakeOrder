from django.contrib import admin
from .models import Category, Product, Volume, PhotosProduct

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class CategotyResorce(resources.ModelResource):
    class Meta:
        model = Category
        fields = ['id','name', 'slug']

class ProductResorce(resources.ModelResource):
    id = fields.Field(column_name='ID продукта',attribute='id')
    category = fields.Field(column_name='Категория', attribute='category', widget=ForeignKeyWidget(Category, 'name'))
    img = fields.Field(column_name='Фото', attribute='img')
    name = fields.Field(column_name='Наименование', attribute='name')
    price = fields.Field(column_name='Цена', attribute='price')
    about1 = fields.Field(column_name='Описание', attribute='about1')
    about2 = fields.Field(column_name='ПЗК', attribute='about2')
    about3 = fields.Field(column_name='Проц. Алкоголь', attribute='about3')
    about4 = fields.Field(column_name='Состав', attribute='about4')
    available = fields.Field(column_name='Наличие 1 или 0', attribute='available')

    class Meta:
        model = Product
        exclude = ['created','uploaded']

class VolumeResorce(resources.ModelResource):
    class Meta:
        model = Volume
        fields = ['name','volume1','volume2','volume3','volume4']
        import_id_fields = ['name']

class PhotosProductResorce(resources.ModelResource):
    class Meta:
        model = PhotosProduct
        fields = ['name','img1','img2','img3','img4']
        import_id_fields = ['name']

class VolumeInline(admin.TabularInline):
    model = Volume

class PhotosProductInline(admin.TabularInline):
    model = PhotosProduct

@admin.register(PhotosProduct)
class PhotosProductAdmin(ImportExportActionModelAdmin):
    resource_class = PhotosProductResorce
    list_display = ['name','img1','img2','img3','img4']

@admin.register(Volume)
class VolumeAdmin(ImportExportActionModelAdmin):
    resource_class = VolumeResorce
    list_display = ['name','volume1','volume2','volume3','volume4']
    list_editable = ['volume1','volume2','volume3','volume4']

@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    resource_class = CategotyResorce
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResorce
    inlines = [PhotosProductInline, VolumeInline]
    list_display = ['id','name', 'slug', 'price', 'available', 'created', 'uploaded']
    list_filter = ['category','available', 'created', 'uploaded']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}
