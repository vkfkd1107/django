from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    chat='hello'
    name='jisu'

    return render(request,'home.html',{'user_chat':chat,'user_name':name})