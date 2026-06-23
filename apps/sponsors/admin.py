"""sponsors admin: sponsor listesi + sponsorluk başvuruları (gelen kutusu)."""

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Sponsor, SponsorshipInquiry


@admin.register(Sponsor)
class SponsorAdmin(TranslationAdmin):
    list_display = ("name", "tier", "url", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("tier", "is_active")
    search_fields = ("name",)


@admin.register(SponsorshipInquiry)
class SponsorshipInquiryAdmin(admin.ModelAdmin):
    """Gelen başvurular: salt-okunur gelen kutusu."""

    list_display = ("name", "organization", "email", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "organization", "email", "message")
    readonly_fields = ("name", "organization", "email", "phone", "message", "created_at")
    list_editable = ("is_read",)
    actions = ["mark_read", "mark_unread"]

    def has_add_permission(self, request):
        return False  # başvurular yalnız form üzerinden gelir

    @admin.action(description="Seçilenleri okundu işaretle")
    def mark_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Seçilenleri okunmadı işaretle")
    def mark_unread(self, request, queryset):
        queryset.update(is_read=False)
