from django.contrib import admin
from .models import Account
# from django.shortcuts import redirect
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# def redirect_if_not_staff(request):
#     if request.user.is_authenticated and not request.user.is_staff:
#         return redirect('home')  # ya koi "not-authorized" page
#     return admin.site.login(request)


class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account,AccountAdmin)

