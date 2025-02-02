# Generated by Django 4.0.3 on 2022-12-10 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_alter_order_delivery_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="base.order",
                verbose_name="Order",
            ),
        ),
    ]
