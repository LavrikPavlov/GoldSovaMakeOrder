
from django.urls import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField('Категория',max_length=50, db_index=True)
    slug = models.SlugField('Товарный слаг', max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"Категория: {self.name}"
    
    def get_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    name = models.CharField('Наименование', max_length=200, db_index=True)
    slug = models.SlugField('Товарный слаг', max_length=200, db_index=True)
    img = models.ImageField('Фото', upload_to='catalog_images',blank=True)
    about1 = models.TextField('Описание', blank=True)
    about2 = models.TextField('Проверенное заводское качество', blank=True)
    about3 = models.TextField('Проц. Алкоголя', blank=True)
    about4 = models.TextField('Состав', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('Наличие', default=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    uploaded = models.DateTimeField('Дата обновления', auto_now=True)
 
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
 
    def __str__(self):
        return f"Продукция: {self.name}"

    def get_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])
    
    
class Volume(models.Model):
    name = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True)
    volume1 = models.BooleanField('0.5л')
    volume2 = models.BooleanField('1.0л')
    volume3 = models.BooleanField('1.5л')
    volume4 = models.BooleanField('50л Кега')

    class Meta:
        verbose_name = 'Обьем'
        verbose_name_plural = 'Обьемы'

    def __str__(self):
        return f"Обьем: {self.name}"
    

class PhotosProduct(models.Model):
    name = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True)
    img1 = models.ImageField('Фото', upload_to='catalog_images',blank=True)
    img2 = models.ImageField('Фото', upload_to='catalog_images',blank=True)
    img3 = models.ImageField('Фото', upload_to='catalog_images',blank=True)
    img4 = models.ImageField('Фото', upload_to='catalog_images',blank=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"Фото: {self.name}"
    
