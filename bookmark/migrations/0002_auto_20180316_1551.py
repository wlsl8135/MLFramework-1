# Generated by Django 2.0.3 on 2018-03-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='url',
            field=models.URLField(unique=True, verbose_name='urlurl'),
        ),
    ]
