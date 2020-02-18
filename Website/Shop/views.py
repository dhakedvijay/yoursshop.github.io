from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *

def Home(request):
    return HttpResponse("This is home page of website")



def Allproduct(request,c_slug=None):
    categ=None
    if c_slug:
        categ=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.filter(category=categ,available=True)
    else:
        products=Product.objects.filter(available=True)
    obj=Category.objects.all()
    print(obj)
    obj1=obj[0]
    obj2=obj[1]
    obj3=obj[2]
    return render(request,'Shop/allproduct.html',{'products':products,'categ':categ,'obj1':obj1,'obj2':obj2,'obj3':obj3})


def Productdetail(request,c_slug=None,p_slug=None):
    product=get_object_or_404(Product,slug=p_slug)
    return render(request,'Shop/productdetail.html',{'product':product})
