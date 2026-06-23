"""Ana Sayfa görünümü — öne çıkan içerikleri toplar."""

from django.shortcuts import render

from apps.competitions.models import Achievement
from apps.sponsors.models import Sponsor
from apps.team.models import Member


def home(request):
    """Ana sayfa: kısa tanıtım + öne çıkan başarılar ve sponsorlar."""
    context = {
        "achievements": Achievement.objects.filter(is_active=True)[:4],
        "sponsors": Sponsor.objects.filter(is_active=True),
        "member_count": Member.objects.filter(is_active=True).count(),
    }
    return render(request, "core/home.html", context)
