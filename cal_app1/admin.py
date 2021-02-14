from django.contrib import admin
from . import models


@admin.register(models.shift)
class shiftoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.arubaito_name)
class arubaito_nameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.time)
class timeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.day)
class dayAdmin(admin.ModelAdmin):
    pass
