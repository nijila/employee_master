from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Employee(models.Model):
    '''An employee's information.'''
    full_name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='employee_images')
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False)
    created_at = models.DateField(default=datetime.date.today)
    
    def __unicode__(self):
        return str(self.full_name)
        # return self.id