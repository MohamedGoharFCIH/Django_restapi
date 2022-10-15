import datetime
from datetime import date
from django.core.validators import MaxValueValidator ,MinLengthValidator
from email import message
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from django.core.validators import RegexValidator

def nameFile(instance, filename):
    return '/'.join(['images', filename])
DISCOUNT_CODE_TYPES_CHOICES = [
    ('percent', 'Percentage-based'),
    ('value', 'Value-based'),
]


# Create your models here
class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, birthday, first_name, last_name, gender, country_code , avatar ,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
   

      
        user = self.model(
            phone_number=self.phone_number,
            birthday=birthday,
            first_name = first_name,
            last_name = last_name,
            gender=gender,
            country_code=country_code,
            avatar = avatar
        )


        user.set_password(password)
        user.save(using=self._db)
        return user

  


class MyUser(AbstractBaseUser):
   

    email = models.EmailField(
        max_length=255,
        unique=True,
        error_messages = { 
        "unique":"taken",
        }

    )

    phone_number = models.CharField(
        max_length=14,
        blank=False,
        null=False,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+[1-9]\d{1,14}$', 
                message="Phone number must be entered in the format E.164'."
            ),
            MinLengthValidator(11)
        ],
        error_messages = {"unique":"taken"}
    )
    
    birthdate = models.DateField( 
        validators=[
            MaxValueValidator(
                limit_value=date.today,
                message="in the future"
                )
            ],
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to=nameFile)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['status', 'birthdate','first_name',  'last_name','country_code', 'gender', 'avatar' ]

    def __str__(self):
        return self.phone_number


  