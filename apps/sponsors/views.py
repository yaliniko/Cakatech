"""Sponsor Ol sayfası: mevcut sponsorlar + başvuru formu."""

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _

from apps.core.notifications import notify_submission

from .forms import SponsorshipForm
from .models import Sponsor


def sponsor_page(request):
    """Sponsorları listele ve sponsorluk başvuru formunu işle."""
    if request.method == "POST":
        form = SponsorshipForm(request.POST)
        if form.is_valid():
            obj = form.save()
            notify_submission(
                subject=f"[Çakatech] Yeni sponsorluk başvurusu: {obj.name}",
                message=(
                    f"{obj.name} ({obj.organization})\n"
                    f"{obj.email} · {obj.phone}\n\n{obj.message}"
                ),
            )
            messages.success(
                request, _("Başvurunuz alındı. Teşekkürler, size dönüş yapacağız.")
            )
            return redirect(reverse("sponsors:page"))
    else:
        form = SponsorshipForm()

    context = {
        "sponsors": Sponsor.objects.filter(is_active=True),
        "form": form,
    }
    return render(request, "sponsors/sponsor_page.html", context)
