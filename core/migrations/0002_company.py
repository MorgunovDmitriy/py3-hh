# Generated by Django 4.2.2 on 2023-06-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=255)),
                ('address_company', models.CharField(max_length=255)),
                ('number_of_employees', models.IntegerField(blank=True, null=True)),
                ('is_hanting', models.BooleanField(default=True)),
            ],
        ),
    ]
