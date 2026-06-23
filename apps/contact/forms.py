"""İletişim formu."""

from django import forms
from django.utils.translation import gettext_lazy as _

from apps.core.forms import HoneypotForm

from .models import ContactMessage


class ContactForm(HoneypotForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": _("Ad Soyad")}),
            "email": forms.EmailInput(attrs={"placeholder": _("E-posta")}),
            "phone": forms.TextInput(attrs={"placeholder": _("Telefon (opsiyonel)")}),
            "subject": forms.TextInput(attrs={"placeholder": _("Konu")}),
            "message": forms.Textarea(attrs={"placeholder": _("Mesajınız"), "rows": 5}),
        }
