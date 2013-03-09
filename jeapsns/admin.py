from django.contrib import admin
from jeapsns.models import post, FollowRelation, msg

admin.site.register(post)
admin.site.register(FollowRelation)
admin.site.register(msg)
