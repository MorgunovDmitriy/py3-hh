
from django.contrib import admin
from django.urls import path
from core.views import *
from core.views import about
from core.views import contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about', about),
    path('contacts', contacts),
    path('adresses', adresses),
]
