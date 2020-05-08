from django.urls import include, path
from django.contrib import admin
from api.models import *

admin.site.register(Administrator)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]