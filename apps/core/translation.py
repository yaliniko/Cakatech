"""core modelleri için çevrilen alanlar (modeltranslation)."""

from modeltranslation.translator import TranslationOptions, register

from .models import PageContent, SiteSettings


@register(SiteSettings)
class SiteSettingsTR(TranslationOptions):
    fields = ("tagline", "about_short", "address", "footer_text")


@register(PageContent)
class PageContentTR(TranslationOptions):
    fields = ("title", "body")
