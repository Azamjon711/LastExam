from django.contrib import admin
from .models import Date, Year, Creator, BlogPost

admin.site.register(Date)
admin.site.register(Year)
admin.site.register(Creator)
admin.site.register(BlogPost)
