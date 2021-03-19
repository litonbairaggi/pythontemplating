from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['name'] = "Liton Bairaggi"
        context['city'] = "Khulna"

        list=[1,2,3,4,5]
        context['list']=list

        return context

class AboutView(TemplateView):
    template_name = "about.html"    

class ContactView(TemplateView):
    template_name = "contact.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['email'] = "liton@gmail.com"
        context['phone'] = "01610202717"
        
        return context    

class BlogView(TemplateView):
    template_name = "blog.html"             