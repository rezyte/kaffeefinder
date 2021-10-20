from django.contrib import admin

from . import models

admin.site.register(models.Cafe)
admin.site.register(models.CafeTag)

