from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

from kaffeefinder.apps.comments.models import Review

User = get_user_model()

class Cafe(models.Model):
    # each manager user is able to have only one cafe instance
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        limit_choices_to=Q( groups__name = 'cafe manager'),
        verbose_name="مدیر کافی شاپ"
    )
    title = models.CharField(max_length=256, verbose_name="نام کافی شاپ")
    description = models.CharField(max_length=1024, verbose_name="توضیحات")
    slug = models.SlugField(allow_unicode=True, verbose_name="نامک")
    address = models.CharField(max_length=512, verbose_name="نشانی")
    image = models.ImageField(upload_to="cafes/%Y/%M/%D")
    tags = models.ManyToManyField("CafeTag", verbose_name="تگ های کافه")

    class Meta:
        verbose_name_plural = "ماژول کافی شاپ ها"

    def __str__(self):
        return self.title

    @property
    def get_address(self):
        try:
            return f"{self.address[:30]} ..."
        except IndexError:
            return self.address

    def latest_comments(self):
        try:
            objects = Review.objects.filter(cafe=self)[:5]
        except IndexError:
            objects = Review.objects.filter(cafe=self)
        return objects


class CafeTag(models.Model):
    title = models.CharField(max_length=64, verbose_name="ویژگی های کافه")
    slug = models.SlugField(null=True, blank=True, verbose_name="نامک ویژگی")
    fa_icon = models.CharField(max_length=32, null=True, blank=True, verbose_name="اسم آیکون فوت آسام")

    def __str__(self):
        return self.title

