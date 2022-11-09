from django.contrib import admin

from .models import Food, Category

for model in [Food, Category]:
    admin.site.register(model)
