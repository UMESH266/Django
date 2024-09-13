from django.contrib import admin
from .models import Articles

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp', 'updated', 'publish']
    search_fields = ['title', 'content']

admin.site.register(Articles, ArticleAdmin)