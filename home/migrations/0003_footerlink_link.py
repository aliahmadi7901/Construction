# Generated by Django 5.0.6 on 2024-07-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_footerlinkscategory_footerlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerlink',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک صفحه'),
        ),
    ]
