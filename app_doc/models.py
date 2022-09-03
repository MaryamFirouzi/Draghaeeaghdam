from email.mime import image
from tkinter import CASCADE
from turtle import title, update
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=50 , null=True)
    address = models.TextField (null=True)
    office_phone1 = models.CharField(max_length=11,null=True)
    office_phone2 = models.CharField(max_length=11,null=True)
    mobile_phone = models.CharField(max_length=11,null=True)
    email = models.EmailField(null=True) 
    top_image = models.ImageField(upload_to='img')
    description = RichTextField(null= True) 

    def __str__(self):
        return self.name


class Top_Image_slider(models.Model):
    top_slider_img = models.ImageField(upload_to='img')
    description = models.TextField(null=True)

    

class Image_slider(models.Model):
    top_image_slider = models.ForeignKey(Top_Image_slider, on_delete=models.CASCADE , null=True)
    slider_img = models.ImageField(upload_to='img') 
    description = models.TextField(null=True)

   
    


class Image_gallery(models.Model):     
    gallery_img = models.ImageField(upload_to='img')  
    description = models.TextField(null=True)

    def __str__(self):
        return self.description
     


class Blog(models.Model):
    title = models.CharField(max_length=50 , null=True)
    image = models.ImageField(upload_to='img') 
    description = RichTextField(null=True )
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogdetail", args=[self.id])

    class meta:
        ordering = ['-updated']     
         
class Question(models.Model):
    question = RichTextField(null=True )
    answer = RichTextField(null=True )

    def __str__(self):
        return 'Question'+str(self.id)
