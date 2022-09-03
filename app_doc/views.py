from bdb import set_trace
from turtle import pd
from django.shortcuts import render

from app_doc.models import Blog, Clinic , Image_slider , Image_gallery, Question , Top_Image_slider
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    top_slider_img = Top_Image_slider.objects.all()
    slider_img = Image_slider.objects.all()
    gallert_img = Image_gallery.objects.all()
    ctx ={
        'clinic' : Clinic.objects.first(),
        'top_slider_img' : top_slider_img ,
        'gallert_img' : gallert_img,
        'slider_img' : slider_img

    }
    
    return render(request, 'home.html',ctx)



def login(request):
    slider_img = Image_slider.objects.all()
    gallert_img = Image_gallery.objects.all()
    ctx ={
        'clinic' : Clinic.objects.first(),
        'slider_img' : slider_img ,
        'gallert_img' : gallert_img

    }
   
    return render(request, 'login.html',ctx)


    
def nobat(request):
    top_slider_img = Top_Image_slider.objects.all()
    slider_img = Image_slider.objects.all()
    gallert_img = Image_gallery.objects.all()
    ctx ={
        'clinic' : Clinic.objects.first(),
        'top_slider_img' : top_slider_img ,
        'gallert_img' : gallert_img,
        'slider_img' : slider_img

    }
    
    return render(request, 'nobat.html',ctx)


    
def blog(request):
    blogs = Blog.objects.all().order_by('-updated')
    paginator = Paginator(blogs,3) # Show 3 blogs per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    ctx ={
        'clinic' : Clinic.objects.first(),
        'blogs' : blogs,
        'page_obj': page_obj
      
    }
    
    return render(request, 'blog.html',ctx)



    
    
def about(request):
    top_slider_img = Top_Image_slider.objects.all()
    slider_img = Image_slider.objects.all()
    gallert_img = Image_gallery.objects.all()
    clinic = Clinic.objects.first()
    ctx ={
        'clinic' : clinic ,
        'top_slider_img' : top_slider_img ,
        'gallert_img' : gallert_img,
        'slider_img' : slider_img
    
    }
    
    return render(request, 'about.html',ctx)


def gallery(request):
    
    gallery = Image_gallery.objects.all()
    ctx ={
        'clinic' : Clinic.objects.first(),
        'gallery' : gallery
        

    }
    
    return render(request, 'gallery.html',ctx)


def contact(request):

    ctx ={
        'clinic' : Clinic.objects.first(),
        

    }
    
    return render(request, 'contact.html',ctx) 


def faq(request):
    question = Question.objects.all()
    
    ctx ={
        'clinic' : Clinic.objects.first(),
        'question' : question ,
        

    }
    
    return render(request, 'faq.html',ctx)  


def blogdetail(request,pk):
    blog = Blog.objects.all()
    thisblog = Blog.objects.get(pk=pk)
    


    ctx ={
        'clinic' : Clinic.objects.first(),
        'thisblog' : thisblog,
        'blog': blog
        
      
    }
    
    return render(request, 'blogdetail.html',ctx)      