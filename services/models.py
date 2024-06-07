from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان سرویس")
    image = models.ImageField(upload_to="services", verbose_name="تصویر سرویس")
    description = models.TextField(verbose_name="توضیحات سرویس")
    short_description = models.CharField(max_length=200, verbose_name="توضیحات کوتاه سرویس")
    possibilities = models.CharField(max_length=300, verbose_name="امکانات سرویس")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'

