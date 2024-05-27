from django.contrib import admin
from .models import *
# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'father_name', 'cnic')

admin.site.register(bioData, MyModelAdmin)