# Generated by Django 2.2.3 on 2019-07-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Allorder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=20)),
                ('customer_id', models.CharField(max_length=250)),
                ('contactno', models.IntegerField()),
            ],
        ),
    ]
