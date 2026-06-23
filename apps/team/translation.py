"""team modelleri için çevrilen alanlar."""

from modeltranslation.translator import TranslationOptions, register

from .models import Member


@register(Member)
class MemberTR(TranslationOptions):
    fields = ("role", "bio")
