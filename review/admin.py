from django.contrib import admin
from .models import Category, Post, Comment, SubCategory, Admin, Contact
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'status', 'slug', 'date_created')
    search_fields = ('author',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Admin)
admin.site.register(Contact)