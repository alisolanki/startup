# Generated by Django 3.0.4 on 2020-04-02 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200402_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeredevent',
            old_name='registeredevent',
            new_name='userprofile',
        ),
    ]