from django.contrib import admin
from mail_sender.models import MessageForAdmin


@admin.register(MessageForAdmin)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('author', 'status', 'date_send')
    search_fields = ('theme', 'author')
    list_filter = ('status',)
    readonly_fields = ('status', 'date_send')
