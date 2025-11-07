from django.db import models

# Create your models here.

#they are python classes 
class UserDetails(models.Model):
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=150,default="user@django.com")
    mobile=models.CharField(max_length=10,null=False,unique=True)


