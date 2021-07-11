from django.contrib import admin
from django.db import models
from . models import studentin
@admin.register(studentin)
class useradmin(admin.ModelAdmin):
    list_display =('id','name','email','password')
