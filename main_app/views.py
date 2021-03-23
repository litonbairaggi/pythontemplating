from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"    

class ContactView(TemplateView):
    template_name = "contact.html"  

class BlogView(TemplateView):
    template_name = "blog.html"  

class Blog_GridView(TemplateView):
    template_name = "blog_grid.html"  

class Blog_ListView(TemplateView):
    template_name = "blog_list.html"             

class Blog_DetailsView(TemplateView):
    template_name = "blog_details.html" 

class ServicesView(TemplateView):
    template_name = "services.html"  

class Services_DetailsView(TemplateView):
    template_name = "services_details.html"             

class GalleryView(TemplateView):
    template_name = "gallery.html"         

class Gallery_02View(TemplateView):
    template_name = "gallery_02.html"             

class Gallery_03View(TemplateView):
    template_name = "gallery_03.html"             

class TestimonialsView(TemplateView):
    template_name = "testimonials.html"             