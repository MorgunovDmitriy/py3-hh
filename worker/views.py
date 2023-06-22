from django.shortcuts import render, HttpResponse
from .models import *

def workers(request):
    workers = Worker.objects.all()  # SElect в Django ORM
    context = {"workers": workers}
    return render(request, 'workers.html', context)
