from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    last_name= models.CharField(max_length=50)
    company = models.CharField(max_length=20)
    email = models.EmailField(max_length=54, unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
          return self.name
