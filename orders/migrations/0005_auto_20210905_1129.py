# Generated by Django 3.2.6 on 2021-09-05 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_customer_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='details',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]