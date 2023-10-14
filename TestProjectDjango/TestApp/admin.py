from django.contrib import admin
from .models import News, Category


class NaewsAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(News)
admin.site.register(Category)
