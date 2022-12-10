# Generated by Django 4.0.3 on 2022-12-10 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('sku', models.CharField(max_length=64, verbose_name='SKU')),
                ('short', models.CharField(blank=True, max_length=256, null=True, verbose_name='Short description')),
                ('full', models.TextField(blank=True, null=True, verbose_name='Short description')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('value', models.CharField(max_length=256, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='base.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product property',
                'verbose_name_plural': 'Products properties',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]