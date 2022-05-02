from math import ceil
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse


from sweetvillaApp .models import Product
def home(request):
    cake=Product.objects.filter(cetegory='cake')
    icecream=Product.objects.filter(cetegory='ice cream')
    punjabi=Product.objects.filter(cetegory='punjabiSweet')
    bengoli=Product.objects.filter(cetegory='bengali sweet')
    sauth=Product.objects.filter(cetegory='sauthindianSweet')
    indian=Product.objects.filter(cetegory='indianSweet')
    gujrati=Product.objects.filter(cetegory='gujratisweet')
    international=Product.objects.filter(cetegory='internationalSweet')
    params={'cake':cake,'ic':icecream,'pb':punjabi,'bs':bengoli,'sauth':sauth,'ind':indian,'gj':gujrati,'inter':international }
    return render(request,'myproj/home.html',params)
def about(request):
    return HttpResponse('this is about')
def contact(request):
    return HttpResponse('this is contact us ')
def tracker(request):
    return HttpResponse('this is tracker ')
def search(request):
    return HttpResponse('search')
def product(request):
    return HttpResponse('this is product')
def checkout(request):
    return HttpResponse('this is checkout')
def feadbaack(request):
    return HttpResponse('this is feadback')
def indianSweet(request):
    products= Product.objects.filter(cetegory='indianSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products,}
    return render(request,'myproj/indian.html',params)
def punjabiSweet(request):
    products= Product.objects.filter(cetegory='punjabiSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/punjabi.html',params)
def sauthIndianSweet(request):
    products= Product.objects.filter(cetegory='sauthindiansweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/sauthindian.html',params)
def bengaliSweet(request):
    products= Product.objects.filter(cetegory='bengali sweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/bengali.html',params)
def internationalsweet(request):
    products= Product.objects.filter(cetegory='internationalSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/international.html',params)
def icecream(request):
    products= Product.objects.filter(cetegory='ice cream')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/icecream.html',params)
def cake(request):
    products= Product.objects.filter(cetegory='cake')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/cake.html',params)
def gujratisweet(request):
    products= Product.objects.filter(cetegory='gujratiSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/cake.html',params)
    






# Create your views here.


# Create your views here.
