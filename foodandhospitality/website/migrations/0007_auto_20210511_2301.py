# Generated by Django 3.2 on 2021-05-11 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='imgupload',
        ),
        migrations.DeleteModel(
            name='userprofile',
        ),
    ]
