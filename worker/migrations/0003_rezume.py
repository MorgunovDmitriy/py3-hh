# Generated by Django 4.2.2 on 2023-06-26 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_worker_user_alter_worker_expested_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('education', models.CharField(max_length=255, verbose_name='Образование')),
                ('work_experience', models.IntegerField(verbose_name='Стаж работы')),
                ('drivers_license', models.BooleanField(default=False, verbose_name='Наличие водительских прав')),
                ('rezume_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.worker')),
            ],
        ),
    ]
