from django.contrib import admin

from .models import *


class GalleryAdmin(admin.TabularInline):
    model = Gallery
    
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'featured_image', 'category', 'location', 'total_likes']

    inlines = [GalleryAdmin]
admin.site.register(Place, PlaceAdmin)


admin.site.register(Category)


class ReplyAdmin(admin.TabularInline):
    model = Reply

class CommentAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'comment', 'place', 'user', 'created_at']

    inlines = [ReplyAdmin]

admin.site.register(Comment, CommentAdmin)