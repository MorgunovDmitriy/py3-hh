from django.shortcuts import render, HttpResponse
from .models import Vacancy

# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse("Найдите работу или работника мечты")

def contacts(request):
    return HttpResponse("<div>Phone: +996777123456 </div> <div>office@handhunter</div>")

def adresses(request):
    return HttpResponse('''
    <ul>
        <li>г.Бишкек, 7 м-н,26/1</li>
        <li>г.ОШ, ул.Мамасалиева 12</li>
        </ul>
    ''')

def vacancy_list(request):
    vacancies=Vacancy.objects.all() #SElect в Django ORM
    context={"vacancies":vacancies}
    context["example"]="Hello World"
    return render(request, 'vacancies.html',context)