from django.contrib import admin
from .models import Category, BlogPost
 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
 
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date")
    list_filter = ("category", "date")
    search_fields = ("title", "description")
 
 