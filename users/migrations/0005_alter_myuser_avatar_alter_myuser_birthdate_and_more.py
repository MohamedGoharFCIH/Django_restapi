# Generated by Django 4.1.2 on 2022-10-15 02:13

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_myuser_email_alter_myuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(error_messages={'blank': 'blank'}, max_length=200, upload_to=''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birthdate',
            field=models.DateField(error_messages={'blank': 'blank'}, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today, message='in the future')]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='country_code',
            field=models.CharField(error_messages={'blank': 'blank'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(error_messages={'blank': 'blank', 'invalid': 'invalid', 'unique': 'taken'}, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(error_messages={'blank': 'blank'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(error_messages={'blank': 'blank'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(error_messages={'blank': 'blank'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(error_messages={'blank': 'blank', 'max_length': {'count': '%(show_value)d', 'error': 'too long'}, 'min_length': {'count': '%(show_value)d', 'error': 'too shoort'}, 'unique': 'taken'}, max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format E.164'.", regex='^\\+[1-9]\\d{1,14}$'), django.core.validators.MinLengthValidator(11)]),
        ),
    ]