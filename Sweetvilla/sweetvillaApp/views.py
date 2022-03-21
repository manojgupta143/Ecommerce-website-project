from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'myproj/home.html')
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
    return render(request,'myproj/indian.html')
def punjabiSweet(request):
    return HttpResponse('this is punjabi sweet')
def sauthIndianSweet(request):
    return render(request,'myproj/sauthindian.html')
def bengaliSweet(request):
    return render(request,'myproj/bengali.html')
def internationalsweet(request):
    return render(request,'myproj/international.html')
def icecream(request):
    return render(request,'myproj/icecream.html')
def cake(request):
    return render(request,'myproj/cake.html')
def gujratisweet(request):
    return render(request,'myproj/gujratisweet.html')






# Create your views here.


# Create your views here.
