from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    married = models.BooleanField(default=False)

class Customers(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=10)

class Products(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)


