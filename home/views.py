from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is Home Page')

def contact(request):
    return render(request, 'contact.html')

def flours(request):
    return render(request, 'flours.html')

def spices(request):
    return render(request, 'spices.html')