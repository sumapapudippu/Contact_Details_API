from django.contrib import admin
from contactbook.models import Contact, ContactDetails

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	list_display = ['frist_name', 'last_name', 'created_at', 'modified_at']

class ContactDetailsAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone_number', 'address', 'created_at', 'modified_at']

admin.site.register(Contact)
admin.site.register(ContactDetails)
