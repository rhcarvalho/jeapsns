from django.contrib import admin
from jeapsns.models import post, FollowRelation, msg


# Normally, class names start with CAPITAL LETTER:
# PostAdmin, Post, ...

class PostAdmin(admin.ModelAdmin):
    # What columns appear in the list of Posts
    list_display = ('author', 'content', 'created')
    #list_display_links = ('author', 'content', 'created')
    list_display_links = list_display
    
    
    # What is the order of fields when EDITING or CREATING a Post
    fields = ('content', 'author')
    
    
    list_filter = ['created', 'author']
    search_fields = ['author', 'content']
    
    # Limit number of Posts per page + PAGINATION (automatic)
    list_per_page = 7
    
    ordering = ["-author"]   # ORDER BY author DESC
    


# class MsgAdmin(admin.ModelAdmin):
#     list_display = ...
#     
#     ...


#admin.site.register(post)   # default configuration
admin.site.register(post, PostAdmin)   # Customized configuration
admin.site.register(FollowRelation)
admin.site.register(msg)
