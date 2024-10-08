# Generated by Django 5.0.6 on 2024-06-30 08:55

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog', verbose_name='مقاله'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childes', to='blog.blogcomment', verbose_name='والد'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='created_time',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت'),
        ),
    ]
