from django.contrib import admin

# Register your models here.
from accidents.models import ranks, types, lists


class ranks_admin(admin.ModelAdmin):
    list_display = ['id' , 'code' , 'name']

admin.site.register(ranks , ranks_admin)

class types_admin(admin.ModelAdmin):
    list_display = ['id' , 'code' , 'name']

admin.site.register(types , types_admin)

class lists_admin(admin.ModelAdmin):
    list_display = ['id' , 'name' ,'address','company_code','company_name','item',\
                    'type_code','type_name','rank_code','rank_name','date','description']

admin.site.register(lists , lists_admin)