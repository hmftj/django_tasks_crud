from django.contrib import admin

# # Register your models here.
#     # your_app/admin.py
from .models import Task
admin.site.register(Task)