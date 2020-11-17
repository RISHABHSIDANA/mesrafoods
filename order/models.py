from django.db import models
from account.models import Account
import datetime    

# Create your models here.


class Restaurant(models.Model):
    restaurant=models.CharField(max_length=120)
    rimage=models.ImageField(upload_to='uploads/restaurants',default=0)
    def __str__(self):
        return self.restaurant
    @staticmethod
    def get_all_restaurants():
        return Restaurant.objects.all()
class Product(models.Model):
    pname=models.CharField(max_length=120)
    price=models.CharField(max_length=120)
    image=models.ImageField(upload_to='uploads/products/')
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)

    def __str__(self):
        return self.pname
    @staticmethod
    def get_all_products_by_id(restaurant_id):
        return Product.objects.filter(restaurant=restaurant_id)    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    @staticmethod
    def get_all_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)

class Myorder(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Account,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Myorder.objects.filter(customer=customer_id).order_by('-date')
