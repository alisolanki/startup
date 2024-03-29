# Generated by Django 3.0.4 on 2020-04-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUserRegisterEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=50)),
                ('eventid', models.CharField(default='null', max_length=50)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('phonenumber', models.CharField(default=0, max_length=13)),
                ('number_of_people', models.IntegerField(default=0)),
                ('username', models.CharField(default='null', max_length=50)),
            ],
        ),
    ]
