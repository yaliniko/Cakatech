"""Takım & Üyeler sayfası."""

from django.shortcuts import render

from .models import Member


def team_list(request):
    """Üyeleri alt takıma göre gruplayarak listele."""
    members = Member.objects.filter(is_active=True)

    # Alt takım sırasına göre grupla (şablonda başlıklı bölümler için)
    groups = []
    for value, label in Member.SubTeam.choices:
        group_members = [m for m in members if m.subteam == value]
        if group_members:
            groups.append({"label": label, "members": group_members})

    return render(request, "team/team_list.html", {"groups": groups})
