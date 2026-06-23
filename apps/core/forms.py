"""Paylaşılan form yardımcıları."""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class HoneypotForm(forms.ModelForm):
    """Basit spam koruması: botların doldurduğu gizli `website` alanı.

    Gerçek kullanıcılar bu alanı görmez (CSS ile gizli). Doluysa form reddedilir.
    """

    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}),
        label="",
    )

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise ValidationError(_("Spam tespit edildi."))
        return ""
