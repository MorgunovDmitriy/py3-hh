from django.shortcuts import render, HttpResponse
from .models import *

def workers(request):
    workers = Worker.objects.all()  # SElect в Django ORM
    context = {"workers": workers}
    return render(request, 'workers.html', context)

def worker_info(request,id):
    worker_object = Worker.objects.get(id=id)
    #SELECT * FROM Worker WHERE id={id}
    vacancies = worker_object.vacancy_set.all()
    context = {
        "worker":worker_object,
        "vacancies": vacancies,
        }
    return render(request, "workerinfo.html", context)