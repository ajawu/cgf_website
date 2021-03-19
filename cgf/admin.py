from django.contrib import admin
from cgf.models import Contact, JoinRequest

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_completed')
    list_editable = ('is_completed',)
    list_filter = ('is_completed',)
    readonly_fields = ('first_name', 'last_name', 'email', 'message')


@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'is_approved')
    list_editable = ('is_approved',)
    list_filter = ('is_approved',)
    readonly_fields = ('full_name', 'email', 'phone_number')
