from django.shortcuts import render
from .models import  Blog

# Create your views here.

def blog(request):
    f=Blog.objects
    return render(request,'blog.html',{'blo':f})