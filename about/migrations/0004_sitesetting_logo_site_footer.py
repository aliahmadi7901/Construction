# Generated by Django 5.0.6 on 2024-07-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_sitesetting_logo_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='logo_site_footer',
            field=models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='لوگوی سایت انتهای صفحه'),
        ),
    ]
