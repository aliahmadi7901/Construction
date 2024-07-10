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


class FooterLinksCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی لینک های پایین صصفحه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'عنوان دسته بندی لینک پایین صفحه'
        verbose_name_plural = 'عنوان دسته بندی لینک های پایین صفحه'


class FooterLink(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان لینک")
    link = models.CharField(max_length=500, verbose_name='لینک صفحه', null=True, blank=True)
    category = models.ForeignKey(
        FooterLinksCategory, on_delete=models.CASCADE, related_name='footer_links', verbose_name="دسته بندی لینک"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لینک پایین صفحه"
        verbose_name_plural = "لینک های پایین صفحه"
