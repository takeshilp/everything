# Generated by Django 3.2.7 on 2021-10-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20211002_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='max_speed',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(default=0, max_length=8, verbose_name='цена'),
        ),
    ]
