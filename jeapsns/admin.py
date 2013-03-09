from django.contrib import admin
from jeapsns.models import post, FollowRelation, msg

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created')
    list_filter = ['created']
    search_fields = ['author', 'content']

admin.site.register(post, PostAdmin)
admin.site.register(FollowRelation)
admin.site.register(msg)
