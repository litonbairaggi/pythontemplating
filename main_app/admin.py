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

@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation', 'facebook', 'linkedin', 'twitter', 'instagram', 'team_img']

@admin.register(Services)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'services_img']

@admin.register(Testimoinials)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'testimoinial_img']

@admin.register(Setting)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phome', 'facebook', 'linkedin', 'twitter', 'instagram', 'company_address', 'logo_img']

@admin.register(Slider)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'sliders_img']
