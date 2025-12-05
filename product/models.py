from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    parent_category=models.ForeignKey('self',on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    created_ar=models.DateField(auto_now=True)
    update_at=models.DateField(auto_created=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)
    price=models.DecimalField(max_digits=10,)
    stock=models.IntegerField(default=0)
    image=models.ImageField( upload_to='products/', )
    created_ar=models.DateField(auto_now=True)
    update_at=models.DateField(auto_created=True)
    def __str__(self):
        return self.name