from django.db import models
from worker.models import Worker
from django.contrib.auth.models import User

class Vacancy(models.Model):
    title = models.CharField(max_length=255,verbose_name='Вакансия')
    salary= models.IntegerField(null=True,blank=True,verbose_name='Зарплата')
    description=models.TextField(default="нет описания",verbose_name='Описание')
    is_relevant=models.BooleanField(default=True, verbose_name='Актуальность')
    email=models.EmailField(verbose_name='Почта')
    contacts=models.CharField(max_length=100, verbose_name='Контакты')
    candidate=models.ManyToManyField(
        to=Worker,
        blank=True,
        )
    view = models.ManyToManyField(
        to=User,
        blank=True,
        verbose_name='Просмотр'
    )
    def __str__(self):
        return self.title

class Company(models.Model):
    name_company = models.CharField(max_length=255,verbose_name='Название компании')
    address_company = models.CharField(max_length=255,verbose_name='Адрес компании')
    number_of_employees= models.IntegerField(null=True,blank=True, verbose_name='Число сотрудников')
    is_hanting=models.BooleanField(default=True,verbose_name='Ищет сотрудников')
    def __str__(self):
        return self.name_company
