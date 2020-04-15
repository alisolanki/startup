# Generated by Django 3.0.4 on 2020-04-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics/place')),
                ('name', models.CharField(default='place-name', max_length=50)),
            ],
        ),
    ]
