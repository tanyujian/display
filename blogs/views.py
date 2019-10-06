from django.shortcuts import render ,get_object_or_404 #获取正文的方法
from .models import  Blog

# Create your views here.

def blog(request):
    f=Blog.objects
    return render(request,'blog.html',{'blo':f})

def ziye(request,blog_id):
    blog_text=get_object_or_404(Blog,pk=blog_id) #获取文本的内容
    return render(request,'textd.html',{'blog':blog_text})