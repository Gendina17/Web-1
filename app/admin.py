from django.contrib import admin
from app import models

admin.site.register(models.Author)
admin.site.register(models.Article)


