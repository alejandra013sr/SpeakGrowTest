from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .models import *

class ExportUser(resources.ModelResource):
    fields = [
        'username','name','email','last_name','phone_number'
    ]

    class Meta:
        model=User


# Register your models here.
class UserProfileAdmin(ImportExportModelAdmin):
    resource_class = ExportUser
    list_display = ('username',)
    search_fields=('username','email')




class AnonymousUserAdmin(admin.ModelAdmin):
    readonly_fields=('created_date','ip_address')
    list_display = ('created_date',)
    list_filter=('ip_address',)

class RoomAdmin(admin.ModelAdmin):
    
    list_display = ('created_date',)
    search_fields=('anonymousUser__ip_address','speaker__username')

admin.site.register(User,UserProfileAdmin)
admin.site.register(AnonymousUser,AnonymousUserAdmin)
admin.site.register(Room,RoomAdmin)