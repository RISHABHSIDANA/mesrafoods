from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from order.models import Product
from order.models import Restaurant,Myorder
from django.contrib.auth.models import User
from order.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
gmail="rr"


# Create your views here.
def index(request):
    r={}
    cart=request.session.get('cart')
    if not cart:
        request.session['cart']={}
    if request.method=="POST":
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        #print('cart' , request.session['cart'])
        return redirect('index')
    rid=request.GET.get('restaurant') 
    #print(rid)
    #print(request.session.get('username'))
    if rid:
      r['products']=Product.get_all_products_by_id(rid)
      r['restaurants']=Restaurant.get_all_restaurants()
      return render(request,'index.html',r)  
    else:
      r['products']=Product.get_all_products()
      r['restaurants']=Restaurant.get_all_restaurants()
      return render(request,'index.html',r)    
def registration(request):
    if request.method == 'POST':
        Name=request.POST['Name']
        Mobile_Number=request.POST['Mobile_Number']
        Password=request.POST['Password']
        #Confirm_Password=request.POST['Confirm_Password']
        myuser=Account.objects.create_user(gmail,Name,Mobile_Number,Password)
        myuser.save()

        return render(request,'login.html')
        
def register(request):
    if request.method == "POST":
        ottp = request.POST.get("ottp")
        print(ottp)
        if ottp == "224243":
            #obj =Email(iemail=gmail)
            #obj.save()
            print(gmail)
            return render(request,'register.html') 
        else:
            return render(request,'email.html')   
    else:
        return HttpResponse("404")        
def handlelogin(request):
   
    return render(request,'login.html')        
def otp(request):
    if request.method == "POST":
        iemail = request.POST.get('iemail')
        global gmail
        gmail=iemail
        #iemail.save()
        print(iemail)
        print(gmail)
        send_mail(
        'Subject',
        'your otp is 224243',
        settings.EMAIL_HOST_USER,
        [iemail],
     )
    
        return render(request,'verify.html')
    else:
        return HttpResponse("404")
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        Pw = request.POST['Pw']
        user =authenticate(username=username,password=Pw)
        if user is not None:
            login(request,user)
            l=Account.objects.return_account_by_email(username)
            print(l)
            request.session['account']=l.id
            return redirect("index")    
        else:
            return HttpResponse("404")  
    else:
        return HttpResponse("404")  
def handlelogout(request):
    logout(request)
    request.session.clear()
    
    return redirect('handlelogin')
def cart(request):
    ids=list(request.session.get('cart').keys())
    products=Product.get_all_products_by_ids(ids)
    u=request.session.get('account')
    print('im',u)
    return render(request,'cart.html',{'products':products})
def checkout(request):
    if request.method == "POST":
       address=request.POST.get('address')
       phone=request.POST.get('phone')
       cart=request.session.get('cart')
       products=Product.get_all_products_by_ids(list(cart.keys()))
       cust= request.session.get('account')
       print(cust)
       for product in products:
            print(cart.get(str(product.id)))
            order = Myorder(customer=Account(id=cust),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.placeOrder()
            request.session['cart'] = {}

    return redirect('cart')
def signup(request):
    return render(request,'email.html')
    


