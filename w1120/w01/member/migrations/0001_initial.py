# Generated by Django 5.1.3 on 2024-11-20 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('nickName', models.CharField(max_length=100)),
                ('cdate', models.DateTimeField(default=datetime.datetime(2024, 11, 20, 10, 9, 16, 103920))),
            ],
        ),
    ]