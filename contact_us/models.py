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
