from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Clinic , Image_gallery, Image_slider , Top_Image_slider , Blog , Question


class Image_sliderInline(admin.TabularInline):
    model = Image_slider
    extra = 1
    

class Top_Image_sliderAdmin(admin.ModelAdmin):
    inlines = [
        Image_sliderInline ,
    ]






admin.site.register(Clinic)
admin.site.register(Top_Image_slider, Top_Image_sliderAdmin )
admin.site.register( Image_gallery)
admin.site.register(Blog)
admin.site.register(Question)