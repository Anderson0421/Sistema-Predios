from django.contrib import admin
from erp.userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email']

admin.site.register(User, UserAdmin)
