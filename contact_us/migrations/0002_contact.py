# Generated by Django 5.0.6 on 2024-07-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('comment', models.TextField(verbose_name='نظر')),
            ],
            options={
                'verbose_name': 'فرم تماس با ما',
                'verbose_name_plural': 'فرم تماس با ما',
            },
        ),
    ]
