from django.contrib import admin

from .models import Food

for model in [Food]:
    admin.site.register(model)
