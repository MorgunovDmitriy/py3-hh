from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(to=User,
                                null=True, blank=False,
                                on_delete=models.CASCADE
                                # приудалении удалить все связанные поля, можно указать SET_NULL(установить ноль)
                                )
    name_worker = models.CharField(max_length=255, verbose_name='ФИО')
    speciality = models.CharField(max_length=255, verbose_name='Специальность')
    expested_salary = models.IntegerField(null=True, blank=True, verbose_name='Ожидаемая зарплата')
    is_searching = models.BooleanField(default=True, verbose_name='Ищет работу')

    def __str__(self):
        return self.name_worker


class Comment(models.Model):
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    to_worker=models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.author.username

class Rezume(models.Model):
    rezume_worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    date_of_birth=models.DateField(verbose_name='Дата рождения')
    education = models.CharField(max_length=255,verbose_name='Образование')
    work_experience = models.IntegerField(verbose_name='Стаж работы')
    drivers_license = models.BooleanField(default=False, verbose_name='Наличие водительских прав')

    def __str__(self):
        return self.rezume_worker.name_worker
