from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):    
    firs_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    Email= models.CharField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return self.firs_name +" "+ self.last_name
    


class Product(models.Model):
    name=models.CharField(max_length=100)
    id=models.AutoField(primary_key=True)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=10000)
    category=models.ForeignKey(Category,default=1,on_delete = models.CASCADE)
    description=models.CharField(max_length=250,default='')
    img=models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.id + " " + self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default='',blank=False)
    phone = models.CharField(max_length=20,blank=False)
    date_time = models.DateField(default= datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product