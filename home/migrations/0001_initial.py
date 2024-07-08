# Generated by Django 5.0.6 on 2024-07-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HappyCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام مشتری')),
                ('comment', models.TextField(verbose_name='نظر مشتری')),
                ('image', models.ImageField(upload_to='customers', verbose_name='عکس مشتری')),
                ('address', models.CharField(max_length=100, verbose_name='آدرس مشتری')),
            ],
            options={
                'verbose_name': 'مشتری خوشحال',
                'verbose_name_plural': 'مشتریان خوشحال',
            },
        ),
    ]
