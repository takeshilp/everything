# Generated by Django 3.2.7 on 2021-10-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20211002_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(default=0, max_length=11, verbose_name='цена'),
        ),
    ]
