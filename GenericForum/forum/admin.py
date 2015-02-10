from django.contrib import admin
from forum.models import Forums, Posts

class forum_admin(admin.ModelAdmin):
    pass
class post_admin(admin.ModelAdmin):
    pass

admin.site.register(Forums, forum_admin)
admin.site.register(Posts, post_admin)