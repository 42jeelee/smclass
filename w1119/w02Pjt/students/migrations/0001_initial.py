# Generated by Django 5.1.3 on 2024-11-19 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('grade', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('age', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1)])),
                ('gender', models.CharField(choices=[('M', '남'), ('F', '여')], max_length=1)),
                ('hobbys', models.CharField(max_length=20)),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('gender__in', ['M', 'F'])), name='check_gender')],
            },
        ),
    ]
