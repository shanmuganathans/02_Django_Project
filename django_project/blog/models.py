from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    published_at = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name
  
