"""core admin: site ayarları (singleton) ve sayfa metinleri."""

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import PageContent, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    """Tek satırlık site ayarları. Eklenemez/silinemez, yalnız düzenlenir."""

    fieldsets = (
        (None, {"fields": ("site_name", "tagline", "about_short")}),
        ("Görseller", {"fields": ("logo", "favicon")}),
        ("İletişim", {"fields": ("email", "phone", "address")}),
        ("Sosyal Medya", {
            "fields": ("instagram_url", "youtube_url", "linkedin_url", "twitter_url"),
        }),
        ("Alt Bilgi", {"fields": ("footer_text",)}),
    )

    def has_add_permission(self, request):
        # Zaten bir satır varsa yenisi eklenemez (singleton)
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PageContent)
class PageContentAdmin(TranslationAdmin):
    list_display = ("label", "key", "title")
    search_fields = ("label", "key", "title")
    readonly_fields = ("key",)  # anahtar şablonlara bağlı; değiştirilemez

    def has_add_permission(self, request):
        # Bloklar migrasyonla tohumlanır; elle eklemeye gerek yok
        return False

    def has_delete_permission(self, request, obj=None):
        return False
