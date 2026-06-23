"""Sponsor modeli ve sponsorluk başvurusu (Sponsor Ol formu)."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import OrderedModel, TimeStampedModel


class Sponsor(OrderedModel):
    """Takımı destekleyen bir sponsor (Sponsor Ol sayfasında listelenir)."""

    class Tier(models.TextChoices):
        PLATINUM = "platinum", _("Platin")
        GOLD = "gold", _("Altın")
        SILVER = "silver", _("Gümüş")
        BRONZE = "bronze", _("Bronz")
        PARTNER = "partner", _("Partner")

    name = models.CharField(_("sponsor adı"), max_length=160)
    logo = models.ImageField(_("logo"), upload_to="sponsors/", blank=True)
    url = models.URLField(_("web sitesi"), blank=True)
    tier = models.CharField(
        _("kategori"), max_length=20, choices=Tier.choices,
        default=Tier.PARTNER, db_index=True,
    )
    description = models.TextField(_("açıklama"), blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsorlar")

    def __str__(self):
        return self.name


class SponsorshipInquiry(TimeStampedModel):
    """'Sponsor Ol' formundan gelen başvuru. Şimdilik yalnızca DB'ye kaydedilir."""

    name = models.CharField(_("ad soyad"), max_length=120)
    organization = models.CharField(_("kurum / firma"), max_length=160, blank=True)
    email = models.EmailField(_("e-posta"))
    phone = models.CharField(_("telefon"), max_length=40, blank=True)
    message = models.TextField(_("mesaj"))
    is_read = models.BooleanField(_("okundu"), default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Sponsorluk Başvurusu")
        verbose_name_plural = _("Sponsorluk Başvuruları")

    def __str__(self):
        return f"{self.name} ({self.organization or self.email})"
