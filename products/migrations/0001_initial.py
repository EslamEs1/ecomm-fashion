# Generated by Django 4.1.3 on 2022-11-06 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branding_name', models.CharField(max_length=50, verbose_name='Branding Name')),
            ],
            options={
                'verbose_name': 'Branding',
                'verbose_name_plural': 'Branding',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description_small', models.TextField(max_length=1000)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('gender', models.CharField(choices=[('ml', 'Male'), ('fm', 'Female')], default='Male', max_length=10)),
                ('description', models.TextField(max_length=15000)),
                ('information', models.TextField(max_length=15000)),
                ('heart', models.IntegerField(default=0, editable=False)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=80, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('branding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branding', to='products.branding')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_img', to='products.product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
