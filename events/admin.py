from django.contrib import admin

# Register your models here.
from events.models import type2, list2


class types_admin(admin.ModelAdmin):
    list_display = ['id' , 'code' , 'name']

admin.site.register(type2 , types_admin)

class lists_admin(admin.ModelAdmin):
    list_display = ['id' , 'name' ,'address','company_code','company_name',\
                    'type_code','type_name','date','description']

admin.site.register(list2 , lists_admin)