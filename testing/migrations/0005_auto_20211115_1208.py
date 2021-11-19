# Generated by Django 3.2.7 on 2021-11-15 11:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_finance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 11, 15, 11, 8, 48, 753987, tzinfo=utc))),
                ('comment', models.TextField(max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.people')),
            ],
        ),
    ]
