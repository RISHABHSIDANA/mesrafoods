from django.contrib import admin
from order.models import Restaurant
from order.models import Product
from order.models import Myorder

admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(Myorder)
