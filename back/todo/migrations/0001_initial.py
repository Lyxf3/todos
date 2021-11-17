# Generated by Django 3.2.7 on 2021-11-16 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True, verbose_name='Title')),
                ('type', models.BooleanField(default=False, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True, verbose_name='Title')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('is_important', models.BooleanField(default=False, verbose_name='Is important')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived')),
                ('type', models.PositiveIntegerField(choices=[(1, 'Pending'), (2, 'In process'), (3, 'Active')], null=True, verbose_name='Type')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Update at')),
            ],
        ),
    ]