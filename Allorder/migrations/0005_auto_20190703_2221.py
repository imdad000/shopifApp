# Generated by Django 2.2.3 on 2019-07-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Allorder', '0004_auto_20190703_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contactno',
            field=models.IntegerField(null=True),
        ),
    ]
