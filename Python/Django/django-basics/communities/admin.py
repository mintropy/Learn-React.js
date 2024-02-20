from django.contrib import admin

from communities.models import Community, Post

# Register your models here.


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "community"]
