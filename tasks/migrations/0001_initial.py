# Generated by Django 5.1.4 on 2025-01-08 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='open', max_length=20)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TaskReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('summary', models.TextField()),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_reports', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='tasks.task')),
            ],
            options={
                'ordering': ['-report_date'],
            },
        ),
    ]
