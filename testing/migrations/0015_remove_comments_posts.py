# Generated by Django 3.2.7 on 2021-11-21 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0014_auto_20211121_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='posts',
        ),
    ]
