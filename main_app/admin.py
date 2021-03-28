from django.contrib import admin

# Register your models here.

from .models import Blog
from .models import Gallery
from .models import Teams
from .models import Services
from . models import Testimoinials
from . models import Setting
from . models import Slider

admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Teams)
admin.site.register(Services)
admin.site.register(Testimoinials)
admin.site.register(Setting)
admin.site.register(Slider)
