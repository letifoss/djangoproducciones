from django.contrib import admin

from .models import Planes
from .models import Mensaje
from .models import Perfil
from .models import Reseña
from .models import Answer

admin.site.register(Planes)
admin.site.register(Mensaje)
admin.site.register(Perfil)
admin.site.register(Reseña)
admin.site.register(Answer)



# Register your models here.
