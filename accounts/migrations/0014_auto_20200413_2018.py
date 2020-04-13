# Generated by Django 3.0.2 on 2020-04-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200402_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredevent',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AddField(
            model_name='registeredevent',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.AddField(
            model_name='registeredevent',
            name='number_of_people',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registeredevent',
            name='phonenumber',
            field=models.CharField(default=0, max_length=13),
        ),
        migrations.AddField(
            model_name='registeredevent',
            name='username',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='registeredevent',
            name='eventid',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
