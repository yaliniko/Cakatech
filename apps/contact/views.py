"""İletişim sayfası ve form işleme."""

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _

from .forms import ContactForm


def contact(request):
    """İletişim formu: gönderimde DB'ye kaydet."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, _("Mesajınız alındı. En kısa sürede dönüş yapacağız.")
            )
            return redirect(reverse("contact:contact"))
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
