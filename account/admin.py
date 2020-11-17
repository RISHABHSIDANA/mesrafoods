from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','username','phonenumber')
    search_fields=('email','username',)
    readonly_fields=('last_login','date_joined')

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Account,AccountAdmin)