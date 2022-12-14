# Generated by Django 4.1.2 on 2022-10-15 02:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_myuser_email_alter_myuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'taken'}, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format E.164'.", regex='^\\+[1-9]\\d{1,14}$'), django.core.validators.MinLengthValidator(11)]),
        ),
    ]
