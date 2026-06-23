"""İletişim formu mesajı modeli."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedModel


class ContactMessage(TimeStampedModel):
    """İletişim formundan gelen mesaj. Şimdilik yalnızca DB'ye kaydedilir."""

    name = models.CharField(_("ad soyad"), max_length=120)
    email = models.EmailField(_("e-posta"))
    phone = models.CharField(_("telefon"), max_length=40, blank=True)
    subject = models.CharField(_("konu"), max_length=160, blank=True)
    message = models.TextField(_("mesaj"))
    is_read = models.BooleanField(_("okundu"), default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("İletişim Mesajı")
        verbose_name_plural = _("İletişim Mesajları")

    def __str__(self):
        return f"{self.name} — {self.subject or self.email}"
