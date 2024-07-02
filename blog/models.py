from django.db import models
from django_jalali.db import models as jmodels


class BlogCategories(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی مقالات"


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    short_descriptions = models.CharField(max_length=200, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='blogs', verbose_name="تصویر مقاله")
    category = models.ForeignKey(
        BlogCategories, on_delete=models.CASCADE, related_name='blogs', verbose_name="دسته بندی مفاله"
    )

    created_time = jmodels.jDateTimeField(auto_now_add=True, verbose_name="زمان ساخت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class BlogComment(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    comment = models.TextField(verbose_name="نظر")
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True, blank=True, related_name='comments', verbose_name='مقاله'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='childes', verbose_name='والد'
    )
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    created_time = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نظر مقاله"
        verbose_name_plural = "نظرات مقاله"
