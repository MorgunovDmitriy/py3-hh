# Generated by Django 4.2.2 on 2023-06-26 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='worker',
            name='expested_salary',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ожидаемая зарплата'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='is_searching',
            field=models.BooleanField(default=True, verbose_name='Ищет работу'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name_worker',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='speciality',
            field=models.CharField(max_length=255, verbose_name='Специальность'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.worker')),
            ],
        ),
    ]
