from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    # table eke penna ona dewal
    list_display =('email','first_name','last_name','last_login','date_joined','is_admin')
    # link ekak click karama details show
    list_display_links=('email' , 'first_name', 'last_name')
    readonly_fields= ('last_login','date_joined')
    ordering =('-date_joined',)

    filter_horizontal =()
    list_filter=()
    fieldsets = ()



admin.site.register(Account ,AccountAdmin)