from django.contrib import admin
from .models import Post, Comment, Tag, Topic

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on', 'updated_at', 'anonymous')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_on', 'updated_at')
    search_fields = ['content', 'author__username'] 

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
