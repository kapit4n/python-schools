from django.contrib import admin
from .models import Hero
from .models import Project

# Register your models here.
admin.site.register(Hero)
admin.site.register(Project)
