# Generated by Django 3.2.4 on 2021-09-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_sys', '0008_alter_bill_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill_order',
            name='finish',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
