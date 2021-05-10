from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class Contact(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    last_name= models.CharField(max_length=250)
    company = models.CharField(max_length=1000)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
          return self.name
