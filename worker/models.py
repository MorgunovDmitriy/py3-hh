from django.db import models


class Worker(models.Model):
    name_worker = models.CharField(max_length=255, verbose_name='ФИО')
    speciality = models.CharField(max_length=255, verbose_name='Специальность')
    expested_salary = models.IntegerField(null=True, blank=True, verbose_name='Ожидаемая зарплата')
    is_searching = models.BooleanField(default=True, verbose_name='Ищет работу')

    def __str__(self):
        return self.name_worker
