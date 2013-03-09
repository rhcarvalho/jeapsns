from django.contrib import admin
from jeapsns.models import post, FollowRelation, msg

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created')

admin.site.register(post, PostAdmin)
admin.site.register(FollowRelation)
admin.site.register(msg)
