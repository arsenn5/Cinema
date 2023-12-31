# Generated by Django 4.2.8 on 2023-12-20 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloth.customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='cloth.product', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(verbose_name='Общая стоимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='cloth.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название тега'),
        ),
    ]
