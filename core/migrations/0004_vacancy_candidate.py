# Generated by Django 4.2.2 on 2023-06-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_worker_user_alter_worker_expested_salary_and_more'),
        ('core', '0003_alter_company_address_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='candidate',
            field=models.ManyToManyField(blank=True, to='worker.worker'),
        ),
    ]
