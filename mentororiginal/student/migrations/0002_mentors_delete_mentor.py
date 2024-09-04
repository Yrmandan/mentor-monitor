# Generated by Django 4.1.3 on 2022-12-01 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=49)),
                ('branch', models.CharField(max_length=98)),
                ('hall_ticket', models.CharField(max_length=10)),
                ('sem_grade', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='mentor',
        ),
    ]
