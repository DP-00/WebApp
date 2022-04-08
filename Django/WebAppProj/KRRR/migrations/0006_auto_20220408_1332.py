# Generated by Django 3.1 on 2022-04-08 11:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('KRRR', '0005_auto_20220406_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sale_price',
            new_name='salePrice',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 13, 32, 32, 222393)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 13, 32, 32, 221391)),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
