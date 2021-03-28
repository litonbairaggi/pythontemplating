from .models import Setting

def settings_processor(request):
 settings = Setting.objects.all()            
 return {'settings': settings}