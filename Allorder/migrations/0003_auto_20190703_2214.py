# Generated by Django 2.2.3 on 2019-07-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Allorder', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
