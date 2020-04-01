# Generated by Django 3.0.4 on 2020-04-01 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200402_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventid', models.IntegerField(default=-1)),
                ('registeredevent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.DeleteModel(
            name='EventsRegistered',
        ),
    ]