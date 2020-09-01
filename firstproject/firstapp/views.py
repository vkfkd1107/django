from django.shortcuts import render
from django.http import HttpResponse
from .models import AiClass

# Create your views here.
students=['jisu','suho','minsu']

def home(request):
    class_object=AiClass.objects.all()

    return render(request,'home.html',{'class_object':class_object})

def result(request):
    name=request.POST['username']

    if name in students:
        is_exist=True
    else:
        is_exist=False
    
    return render(request,'result.html',{'user_name':name,'is_exist':is_exist})