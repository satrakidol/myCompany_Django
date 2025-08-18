from django.contrib import admin
from .models import Employees, Customers, Products

# Register your models here.
admin.site.register(Employees)
admin.site.register(Customers)
admin.site.register(Products)
