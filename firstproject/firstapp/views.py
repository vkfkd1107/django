from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

students=['jisu','minso','suho']

def home(request):
    chat='hello'
    name='jisu'

    return render(request,'home.html',{'user_chat':chat,'user_name':name})

def result(request):
    name=request.POST['username']

    if name in students:
        is_exist=True
    else:
        is_exist=False
    
    return render(request,'result.html',{'user_name':name,'is_exist':is_exist})