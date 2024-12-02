from django.contrib import admin
from .models import Question, Choice  # Import your models

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)