from django.contrib import admin

# Register your models here.
from competition.models import PhotoPost, Comment, Like


@admin.register(PhotoPost)
class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description', 'status')
    list_display_links = ('id', 'title', 'image', 'description')
    search_fields = ('title', 'status', 'description', 'published_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_date', 'content_object')
    list_display_links = ('id', 'content', 'created_date', 'content_object')
    search_fields = ('content', 'created_date')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    list_display_links = ('id', 'user', 'post')
    search_fields = ('user', 'post')