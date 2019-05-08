from django.contrib import admin

# Register your models here.
from events.models import types, lists


class types_admin(admin.ModelAdmin):
    list_display = ['id' , 'code' , 'name']

admin.site.register(types , types_admin)

class lists_admin(admin.ModelAdmin):
    list_display = ['id' , 'name' ,'address','company_code','company_name',\
                    'type_code','type_name','date','description']

admin.site.register(lists , lists_admin)