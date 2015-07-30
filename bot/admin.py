from django.contrib import admin
from .models import *

class MessageAdmin(admin.ModelAdmin):
    list_display=('message','username','date')

    def username(self, obj):
        return obj.user.username
admin.site.register(Message, MessageAdmin)
admin.site.register([ Response, Update])
