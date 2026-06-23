"""competitions modelleri için çevrilen alanlar."""

from modeltranslation.translator import TranslationOptions, register

from .models import Achievement, Competition


@register(Competition)
class CompetitionTR(TranslationOptions):
    fields = ("name", "location", "description", "result")


@register(Achievement)
class AchievementTR(TranslationOptions):
    fields = ("title", "description")
