from django.contrib import admin

# Register your models here.
from users.models import users


class users_admin(admin.ModelAdmin):
    list_display = ['id','code','name','sex','birthday','company_code','company_name','position',\
                   'entrytime', 'email','telephone','password']

admin.site.register(users, users_admin)