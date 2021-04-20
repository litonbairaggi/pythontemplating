from django.contrib import admin

# Register your models here.

from .models import Blog
from .models import Gallery
from .models import Teams
from .models import Services
from . models import Testimoinials
from . models import Setting
from . models import Slider

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'blog_img']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gallery_img']
    
admin.site.register(Teams)
admin.site.register(Services)
admin.site.register(Testimoinials)
admin.site.register(Setting)
admin.site.register(Slider)
