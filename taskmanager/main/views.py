from django.shortcuts import render
# Create your views here.
#from django.http import HttpResponse


def index(request):
    return render(request,'main/index.html')
def about(request):
    return render(request,'main/about.html')
def news(request):
    return render(request,'main/news.html')
def support(request):
    return render(request,'main/support.html')
def tours(request):
    return render(request,'main/tours.html')
def products(request):
    return render(request,'main/products.html')
def maybe(request):
    return render(request,'main/maybe.html')
def empty(request):
    return render(request,'main/empty.html')
# /---\
#  0-0
#   |
# /|||\
#/ ||| \
# /   \
