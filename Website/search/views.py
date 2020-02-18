from django.shortcuts import render
from Shop.models import Product
from django.http import HttpResponse
from django.db.models  import Q


def Search(request):
    products=None
    query=None
    print('q' in request.POST)
    if 'q' in request.POST:
        query=request.POST.get('q')
        print("BBB",query)
        products=Product.objects.all().filter(Q(description__contains=query) | Q(name__contains=query))
    print("AAAA",products)
    print("BBB",query)
    return render(request,'search/search.html',{'query':query,'products':products})
