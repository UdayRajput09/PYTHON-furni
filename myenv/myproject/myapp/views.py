from django.shortcuts import render, redirect
from .models import *
import random
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def services(request):
    return render(request, 'services.html')

def shop(request):
    return render(request, 'shop.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Email already exists!"
            return render(request, 'signup.html', {'msg': msg})
        except User.DoesNotExist:
            if request.POST['password'] == request.POST['CPassword']:
                User.objects.create(
                    name=request.POST['name'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    mobile=request.POST['mobile'],
                    profile=request.FILES['profile'],
                    userType=request.POST['userType']
                )
                return render(request, 'login.html')
            else:
                msg = "Password and Confirm Password do not match!"
                return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                request.session['email'] = user.email
                request.session['profile'] = user.profile.url
                if user.userType == "buyer":
                    return render(request, "index.html")
                else:
                    return render(request, "seller_index.html")
            else:
                msg = "Password does not match!"
                return render(request, "login.html", {'msg': msg})
        except User.DoesNotExist:
            msg = "Email does not exist!"
            return render(request, "login.html", {'msg': msg})
    else:
        return render(request, 'login.html')

def logout(request):
    del request.session['email']
    del request.session['profile']
    return redirect('login')

def cpass(request):
    user = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        try:
            if user.password == request.POST['password']:
                if request.POST['npassword'] == request.POST['cnpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return redirect('logout')
                else:
                    msg = "New password and Confirm Password do not match!"
                    if user.userType == "buyer":
                        return render(request, 'cpass.html', {'msg': msg})
                    else:
                        return render(request, 'seller_cpass.html', {'msg': msg})
            else:
                msg = "Old password does not match!"
                if user.userType == "buyer":
                    return render(request, "cpass.html", {'msg': msg})
                else:
                    return render(request, 'seller_cpass.html', {'msg': msg})
        except:
            if user.userType == "buyer":
                return render(request, "cpass.html")
            else:
                return render(request, 'seller_cpass.html')
    else:
        if user.userType == "buyer":
            return render(request, "cpass.html")
        else:
            return render(request, 'seller_cpass.html')

def fpass(request):
    if request.method == "POST":
        user = User.objects.get(mobile=request.POST['mobile'])
        mobile = request.POST['mobile']
        otp = random.randint(1001, 9999)
        url = "https://www.fast2sms.com/dev/bulkV2"
        querystring = {
            "authorization": "EM5TxhCfzI9UyJ80Niw7soGmOrVaAbtQ3nFZeRYqdB2KgWv61ikQ0M538obtfGCvKAlR7xrVXF6mOy9",
            "variables_values": otp,
            "route": "otp",
            "numbers": str(mobile)
        }
        headers = {
            'cache-control': "no-cache"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        request.session['mobile'] = mobile
        request.session['otp'] = otp
        return render(request, 'otp.html')
    else:
        return render(request, 'fpass.html')

def profile(request):
    user = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.mobile = request.POST['mobile']
        try:
            user.profile = request.FILES['profile']
            user.save()
            request.session['profile'] = user.profile.url
        except:
            user.save()
            if user.userType == "buyer":
                return redirect('index')
            else:
                return redirect('seller_index') 
    else:
        if user.userType == "buyer":
            return render(request, 'profile.html', {'user': user})
        else:
            return render(request,'seller_profile.html',{'user':user})   
        


def seller_index(request):
    return render(request, 'seller_index.html')


def seller_cpass(request):
    return render(request,'seller_cpass.html')



def seller_addproduct(request):
     if request.method == "POST":
        user = User.objects.get(email=request.session['email'])
        try:
            print("hello")
            Product.objects.create(
                user=user,
                pcategory=request.POST['pcategory'],
                pname=request.POST['pname'],
                pprice=request.POST['pprice'],
                pdesc=request.POST['pdesc'],
                pimg=request.FILES['pimg'], 
            )
            return redirect("seller_viewproduct")
        except Exception as e:
            print(e)
            msg = "Error adding product. Please try again."
            return render(request, "seller_index.html", {"msg": msg})
     else:
        return render(request,'seller_addproduct.html')


def seller_viewproduct(request):
    return render(request,'seller_viewproduct.html')