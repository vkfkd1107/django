from django.shortcuts import render
from django.http import HttpResponse
from .models import AiClass

# Create your views here.
students=['jisu','suho','minsu']

def home(request):
    classes=AiClass.objects.all()

    context={
        'classes':classes
    }

    return render(request,'home.html',context)