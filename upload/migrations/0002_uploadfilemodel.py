# Generated by Django 2.0.3 on 2018-03-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
