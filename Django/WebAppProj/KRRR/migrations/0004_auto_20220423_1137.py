# Generated by Django 3.1 on 2022-04-23 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KRRR', '0003_auto_20220421_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 11, 37, 34, 376448)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 11, 37, 34, 375445)),
        ),
        migrations.AlterField(
            model_name='product',
            name='salePrice',
            field=models.IntegerField(null=True),
        ),
    ]
