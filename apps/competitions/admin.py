"""competitions admin."""

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Achievement, Competition


@admin.register(Competition)
class CompetitionAdmin(TranslationAdmin):
    list_display = ("name", "season", "date", "result", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("season", "is_active")
    search_fields = ("name", "location", "result")


@admin.register(Achievement)
class AchievementAdmin(TranslationAdmin):
    list_display = ("title", "date", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
