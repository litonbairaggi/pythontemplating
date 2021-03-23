from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/',views.HomeView.as_view(), name="/"),
    path('about/',views.AboutView.as_view(), name="about"),
    path('contact/',views.ContactView.as_view(), name="contact"),

    path('blog/',views.BlogView.as_view(), name="blog"),
    path('blog_grid/',views.Blog_GridView.as_view(), name="blog_grid"),
    path('blog_list/',views.Blog_ListView.as_view(), name="blog_list"),
    path('blog_details/',views.Blog_DetailsView.as_view(), name="blog_details"),
    path('services/',views.ServicesView.as_view(), name="services"),
    path('services_details/',views.Services_DetailsView.as_view(), name="services_details"),
    path('gallery_01/',views.GalleryView.as_view(), name="gallery_01"),
    path('gallery_02/',views.Gallery_02View.as_view(), name="gallery_02"),
    path('gallery_03/',views.Gallery_03View.as_view(), name="gallery_03"),
    path('testimonials/',views.TestimonialsView.as_view(), name="testimonials"),

]