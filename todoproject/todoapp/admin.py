from django.contrib import admin

# Register your models here.
from todoapp.models import Tasks

admin.site.register(Tasks)