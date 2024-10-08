# Generated by Django 5.0.6 on 2024-06-02 10:04

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی پروژه',
                'verbose_name_plural': 'دسته بندی های پروژه',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان پروژه')),
                ('image', models.ImageField(upload_to='media/project', verbose_name='نصویر پروژه')),
                ('short_description', models.CharField(max_length=200, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('customer_name', models.CharField(max_length=200, verbose_name='نام مشتری')),
                ('project_type', models.CharField(max_length=200, verbose_name='نوع پروژه')),
                ('created_time', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='زمان شروع پروژه')),
                ('finish_time', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='زمان پایان پروژه')),
                ('project_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='projects.projectcategory', verbose_name='دسته بندی پروژه')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
            },
        ),
        migrations.CreateModel(
            name='ProjectGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/project', verbose_name='تصویر')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_galleries', to='projects.project', verbose_name='پروژه')),
            ],
            options={
                'verbose_name': 'گالری تصویر',
                'verbose_name_plural': 'گالری تصاویر',
            },
        ),
    ]
