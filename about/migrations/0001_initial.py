# Generated by Django 5.0.6 on 2024-07-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_success_count', models.IntegerField(verbose_name='تعداد پزوژه های موفق')),
                ('rebuilding_count', models.IntegerField(verbose_name='تعداد بازسازی ها')),
                ('zero_to_hundred_count', models.IntegerField(verbose_name='تعداد صفر تا صد ها')),
                ('copy_right_text', models.TextField(verbose_name='متن کپی رایت سایت')),
                ('footer_text', models.TextField(verbose_name='متن پاورقی سایت')),
                ('film_link', models.CharField(max_length=300, verbose_name='لینک فیلم تبلیغاتی')),
            ],
            options={
                'verbose_name': 'تنظبمات سایت',
                'verbose_name_plural': 'تنظیمات سایت ',
            },
        ),
    ]
