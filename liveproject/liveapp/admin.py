from django.contrib import admin
from liveapp.models import student

# Register your models here.

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=["id","roll","name","email","phone"]
    