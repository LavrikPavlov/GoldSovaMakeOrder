# Generated by Django 4.1.7 on 2023-05-11 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=200, verbose_name='Товарный слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=200, verbose_name='Товарный слаг')),
                ('img', models.ImageField(blank=True, upload_to='catalog_images', verbose_name='Фото')),
                ('about1', models.TextField(blank=True, verbose_name='Описание')),
                ('about2', models.TextField(blank=True, verbose_name='Проверенное заводское качество')),
                ('about3', models.TextField(blank=True, verbose_name='Проц. Алкоголя')),
                ('about4', models.TextField(blank=True, verbose_name='Состав')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('uploaded', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукция',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='PhotosProduct',
            fields=[
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalog.product')),
                ('img1', models.ImageField(blank=True, upload_to='catalog_images', verbose_name='Фото')),
                ('img2', models.ImageField(blank=True, upload_to='catalog_images', verbose_name='Фото')),
                ('img3', models.ImageField(blank=True, upload_to='catalog_images', verbose_name='Фото')),
                ('img4', models.ImageField(blank=True, upload_to='catalog_images', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalog.product')),
                ('volume1', models.BooleanField(verbose_name='0.5л')),
                ('volume2', models.BooleanField(verbose_name='1.0л')),
                ('volume3', models.BooleanField(verbose_name='1.5л')),
                ('volume4', models.BooleanField(verbose_name='50л Кега')),
            ],
            options={
                'verbose_name': 'Обьем',
                'verbose_name_plural': 'Обьемы',
            },
        ),
    ]
