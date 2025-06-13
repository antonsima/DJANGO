from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    exclude = ("password",)
