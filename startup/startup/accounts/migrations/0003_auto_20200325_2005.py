# Generated by Django 3.0.2 on 2020-03-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(upload_to='pics/accounts'),
        ),
    ]
