from django.shortcuts import  render
from gallery.models import  Gallery


g=Gallery.objects  #获取model中的内容

def home(request):
    return render(request,'home.html',{'gallerys':g})