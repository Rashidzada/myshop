from django.contrib import admin
from .import models
# Register your models here.
@admin.register(models.Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('name','email','subject','message')