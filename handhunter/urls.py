from django.contrib import admin
from django.urls import path
from core.views import *
from worker.views import *
from worker.views import worker_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about', about),
    path('contacts', contacts),
    path('adresses', adresses),
    path('vacancies', vacancy_list),
    path('companys', company),
    path('workers', workers),
    path ('worker/<int:id>', worker_info),
]
