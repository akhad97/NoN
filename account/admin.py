from django.contrib import admin


# Register your models here.
from account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'age', 'gender', 'contact_number']

