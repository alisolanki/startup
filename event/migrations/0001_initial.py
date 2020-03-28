# Generated by Django 2.2.6 on 2020-03-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(default='event-name', max_length=50)),
                ('slug', models.CharField(default='name%place%01%01%2001%', max_length=50)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]