from django.db import models


class ContactUs(models.Model):
    address = models.CharField(max_length=300, verbose_name='آدرس')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس')
    instagram = models.CharField(max_length=100, verbose_name='اینستاگرام')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    comment = models.TextField(verbose_name='نظر')
    checked = models.BooleanField(default=False, verbose_name='چک شده/نشده')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فرم تماس با ما'
        verbose_name_plural = 'فرم تماس با ما'
