from django.contrib import admin
from django.urls import path
from order import views


urlpatterns = [
    
   
    path('', views.index,name="index"),
    path('signup', views.signup,name="signup"),
    path('register',views.register,name="register"),
    path('otp',views.otp,name="otp"),
    path('home',views.home,name="home"),
    path('registration',views.registration,name="registration"),
    path('handlelogin',views.handlelogin,name="handlelogin"),
    path('handlelogout',views.handlelogout,name="handlelogout"),
    path('cart', views.cart,name="cart"),
    path('checkout', views.checkout,name="checkout"),
    
    
]
