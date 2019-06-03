from django.contrib import admin

# Register your models here.
from .models import Board	

# add Board model
admin.site.register(Board)