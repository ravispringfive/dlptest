from django.contrib import admin
from dlpApp.models import TestUser


class TestUserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'age', 'gender']


admin.site.register(TestUser, TestUserAdmin)
