from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class Cafe(models.Model):
    # each manager user is able to have only one cafe instance
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE,
        limit_choices_to=Q( groups__name = 'cafe manager'),
        verbose_name="مدیر کافی شاپ"
    )
    title = models.CharField(max_length=256, verbose_name="نام کافی شاپ")
    description = models.CharField(max_length=1024, verbose_name="توضیحات")
    slug = models.SlugField(allow_unicode=True, verbose_name="نامک")
    address = models.CharField(max_length=512, verbose_name="نشانی")
    image = models.ImageField(upload_to="cafes/%Y/%M/%D")

    class Meta:
        verbose_name_plural = "ماژول کافی شاپ ها"

    def __str__(self):
        return self.title
