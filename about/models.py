from django.db import models


class SiteSetting(models.Model):
    project_success_count = models.IntegerField(verbose_name='تعداد پزوژه های موفق')
    rebuilding_count = models.IntegerField(verbose_name='تعداد بازسازی ها')
    zero_to_hundred_count = models.IntegerField(verbose_name='تعداد صفر تا صد ها')
    copy_right_text = models.TextField(verbose_name='متن کپی رایت سایت')
    footer_text = models.TextField(verbose_name='متن پاورقی سایت')
    film_link = models.CharField(max_length=300, verbose_name='لینک فیلم تبلیغاتی')

    def __str__(self):
        return self.copy_right_text

    class Meta:
        verbose_name = 'تنظبمات سایت'
        verbose_name_plural = 'تنظیمات سایت '


class TeamMembers(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    image = models.ImageField(upload_to='team_members', verbose_name='تصویر')
    skill = models.CharField(max_length=100, verbose_name='مهارت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اعضای تیم'
        verbose_name_plural = 'اعضا های تیم'

