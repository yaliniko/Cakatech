"""team admin."""

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Member


@admin.register(Member)
class MemberAdmin(TranslationAdmin):
    list_display = ("name", "role", "subteam", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("subteam", "is_active")
    search_fields = ("name", "role")
