from django.db import models
from django_jalali.db import models as jmodels


class ProjectCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی پروژه"
        verbose_name_plural = "دسته بندی های پروژه"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    image = models.ImageField(upload_to='project', verbose_name="نصویر پروژه")
    short_description = models.CharField(max_length=200, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name="توضیحات")
    customer_name = models.CharField(max_length=200, verbose_name="نام مشتری")
    project_type = models.CharField(max_length=200, verbose_name="نوع پروژه")
    created_time = jmodels.jDateTimeField(null=True, blank=True, verbose_name="زمان شروع پروژه")
    finish_time = jmodels.jDateTimeField(null=True, blank=True, verbose_name="زمان پایان پروژه")
    project_category = models.ForeignKey(
        ProjectCategory, on_delete=models.PROTECT, related_name='projects', verbose_name="دسته بندی پروژه"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"


class ProjectGallery(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_galleries", verbose_name="پروژه"
    )
    image = models.ImageField(upload_to="media/project", verbose_name="تصویر")

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = "گالری تصویر"
        verbose_name_plural = "گالری تصاویر"
