"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from.import views
# from myapp import views

urlpatterns = [

    ## Buyer ##
     
     path('index/', views.index, name='index'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('blog/', views.blog, name='blog'),
     path('cart/', views.cart, name='cart'),
     path('checkout/', views.checkout, name='checkout'),
     path('services/', views.services, name='services'),
     path('shop/', views.shop, name='shop'),
     path('thankyou/', views.thankyou, name='thankyou'),
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('cpass/', views.cpass, name='cpass'),
     path('fpass/', views.fpass, name='fpass'),
     path('profile/', views.profile, name='profile'),


    ## Seller ##

    path('seller_index/', views.seller_index, name='seller_index'),
    path('seller_addproduct/', views.seller_addproduct, name='seller_addproduct'),
    path('seller_viewproduct/', views.seller_viewproduct, name='seller_viewproduct'),
]
