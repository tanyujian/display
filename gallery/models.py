from django.db import models

# Create your models here.

class Gallery(models.Model):


    discription= models.CharField(max_length=50) #创建一个文本框

    picture=models.ImageField (default= 'default.png',upload_to='image/')

    title= models.CharField(default='作品', max_length=50)
    def __str__(self):
        return self.title