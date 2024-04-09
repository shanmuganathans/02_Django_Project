from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name
    
    