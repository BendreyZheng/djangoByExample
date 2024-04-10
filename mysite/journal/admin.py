from django.contrib import admin
from .models import JournalProfile

# Register your models here.
@admin.register(JournalProfile)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name','ranking', 'user', 'status']
    list_filter = ['status']
    search_fields = ['name']
    raw_id_fields = ['user']
    ordering = ['status', 'ranking']