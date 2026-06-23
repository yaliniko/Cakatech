"""sponsors modelleri için çevrilen alanlar."""

from modeltranslation.translator import TranslationOptions, register

from .models import Sponsor


@register(Sponsor)
class SponsorTR(TranslationOptions):
    fields = ("description",)
