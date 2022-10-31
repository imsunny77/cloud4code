from django.contrib import admin
from .models import *

class RootUserAdmin(admin.ModelAdmin):
    fields = ['email','first_name', 'last_name']

admin.site.register(RootUser,RootUserAdmin)
