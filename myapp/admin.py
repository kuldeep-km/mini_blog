from django.contrib import admin
from myapp.models import BlogModel

# Register your models here.
admin.site.register(BlogModel)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content', 'publication_date']