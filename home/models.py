from django.db import models


class HappyCustomers(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام مشتری')
    comment = models.TextField(verbose_name='نظر مشتری')
    image = models.ImageField(upload_to='customers', verbose_name='عکس مشتری')
    address = models.CharField(max_length=100, verbose_name='آدرس مشتری')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مشتری خوشحال'
        verbose_name_plural = 'مشتریان خوشحال'

