# Generated by Django 3.1 on 2022-04-14 10:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KRRR', '0007_auto_20220408_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'still shopping'), ('paid', 'shopping compleated'), ('done', 'order compleated')], default='cart', max_length=4),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 12, 13, 38, 409030)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 12, 13, 38, 408032)),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KRRR.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KRRR.product')),
            ],
        ),
    ]
