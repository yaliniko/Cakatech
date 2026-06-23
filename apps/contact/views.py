"""İletişim sayfası ve form işleme."""

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _

from apps.core.notifications import notify_submission

from .forms import ContactForm


def contact(request):
    """İletişim formu: gönderimde DB'ye kaydet (+ etkinse e-posta bildirimi)."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save()
            notify_submission(
                subject=f"[Çakatech] Yeni iletişim mesajı: {obj.subject or obj.name}",
                message=f"{obj.name} <{obj.email}>\n\n{obj.message}",
            )
            messages.success(
                request, _("Mesajınız alındı. En kısa sürede dönüş yapacağız.")
            )
            return redirect(reverse("contact:contact"))
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
