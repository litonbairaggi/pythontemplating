from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from . models import Blog
from . models import Teams
from .models import Gallery
from .models import Services
from .models import Testimoinials
from .models import Setting
from . models import Slider

class HomeView(TemplateView):
    template_name = "index.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['blogs'] = Blog.objects.all().order_by('id')[:2]
        context['teams'] = Teams.objects.all().order_by('id')[:4]
        context['gallerys'] = Gallery.objects.all().order_by('-id')[:8]
        context['services'] = Services.objects.all().order_by('id')[:3]
        context['testimoinials'] = Testimoinials.objects.all()
        context['settings'] = Setting.objects.all()
        context['sliders'] = Slider.objects.all().order_by('id')[:3]

        return context 

class AboutView(TemplateView):
    template_name = "about.html"   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Teams.objects.all().order_by('id')[:4]
        return context 

class ContactView(TemplateView):
    template_name = "contact.html"  

class BlogView(TemplateView):
    template_name = "blog.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('id')[:4]
        return context

class Blog_GridView(TemplateView):
    template_name = "blog_grid.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('id')[:8]
        return context


class Blog_ListView(TemplateView):
    template_name = "blog_list.html"   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('id')[:4]
        return context          

class Blog_DetailsView(TemplateView):
    template_name = "blog_details.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('id')[:1]
        return context 

class ServicesView(TemplateView):
    template_name = "services.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all().order_by('id')[:6]
        return context 

class Services_DetailsView(TemplateView):
    template_name = "services_details.html"             

class GalleryView(TemplateView):
    template_name = "gallery.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all().order_by('id')[:16]
        return context 

class Gallery_02View(TemplateView):
    template_name = "gallery_02.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all().order_by('-id')[:16]
        return context             

class Gallery_03View(TemplateView):
    template_name = "gallery_03.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all().order_by('id')[:16]
        return context            

class TestimonialsView(TemplateView):
    template_name = "testimonials.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimoinials'] = Testimoinials.objects.all().order_by('-id')
        return context 

class ContactView(TemplateView):
    template_name = "contact.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Setting.objects.all()
        return context 


# class SettingView(TemplateView):
#     template_name = "base.html"  

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['settings'] = Setting.objects.all()
#         return context
