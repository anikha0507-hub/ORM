from django.db import models
from django.contrib import admin
class product(models.Model):
    productID=models.CharField(primary_key=True,max_length=7)
    productname=models.CharField(max_length=30)
    dept=models.CharField(max_length=20)
    productbrand=models.CharField(max_length=20)
    Dateofexpi=models.DateField()
    Dateofdeli=models.DateField()
    price=models.IntegerField()

class productAdmin(admin.ModelAdmin):
    list_display=["productID","productname","dept","productbrand","Dateofexpi","Dateofdeli","price"]

