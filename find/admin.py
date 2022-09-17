from django.contrib import admin

# Register your models here.
from .models import Games, Comment, Bar


admin.site.register(Bar)
admin.site.register(Comment)
admin.site.register(Games)