"""Yarışmalar & Başarılar sayfası."""

from django.shortcuts import render

from .models import Achievement, Competition


def competitions_list(request):
    context = {
        "competitions": Competition.objects.filter(is_active=True),
        "achievements": Achievement.objects.filter(is_active=True),
    }
    return render(request, "competitions/competitions_list.html", context)
