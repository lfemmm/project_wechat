from django.contrib import admin

# Register your models here.
from company.models import company


class company_admin(admin.ModelAdmin):
    list_display = ['id','code','name','description']

admin.site.register(company , company_admin)