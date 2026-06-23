"""contact admin: iletişim mesajları gelen kutusu."""

from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Gelen mesajlar: salt-okunur gelen kutusu."""

    list_display = ("name", "subject", "email", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "phone", "subject", "message", "created_at")
    list_editable = ("is_read",)
    actions = ["mark_read", "mark_unread"]

    def has_add_permission(self, request):
        return False

    @admin.action(description="Seçilenleri okundu işaretle")
    def mark_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Seçilenleri okunmadı işaretle")
    def mark_unread(self, request, queryset):
        queryset.update(is_read=False)
