"""Sponsorluk başvuru formu."""

from django import forms
from django.utils.translation import gettext_lazy as _

from apps.core.forms import HoneypotForm

from .models import SponsorshipInquiry


class SponsorshipForm(HoneypotForm):
    class Meta:
        model = SponsorshipInquiry
        fields = ["name", "organization", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": _("Ad Soyad")}),
            "organization": forms.TextInput(attrs={"placeholder": _("Kurum / Firma")}),
            "email": forms.EmailInput(attrs={"placeholder": _("E-posta")}),
            "phone": forms.TextInput(attrs={"placeholder": _("Telefon (opsiyonel)")}),
            "message": forms.Textarea(
                attrs={"placeholder": _("Nasıl destek olmak istersiniz?"), "rows": 5},
            ),
        }
