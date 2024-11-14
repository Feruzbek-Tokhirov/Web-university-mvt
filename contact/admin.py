from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "is_published")
    list_filter = ("is_published", )
    search_fields = ("name", "phone")


admin.site.register(Contact, ContactAdmin)
