# Generated by Django 3.2.7 on 2021-11-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20211114_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
