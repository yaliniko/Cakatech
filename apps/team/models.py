"""Takım üyeleri modeli."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import OrderedModel


class Member(OrderedModel):
    """Bir takım üyesi (Takım & Üyeler sayfası)."""

    class SubTeam(models.TextChoices):
        CAPTAIN = "captain", _("Kaptan")
        MENTOR = "mentor", _("Mentor")
        MECHANICAL = "mechanical", _("Mekanik")
        SOFTWARE = "software", _("Yazılım")
        DESIGN = "design", _("Tasarım / CAD")
        MEDIA = "media", _("Medya")
        BUSINESS = "business", _("İş Geliştirme")

    name = models.CharField(_("ad soyad"), max_length=120)
    role = models.CharField(_("görev / unvan"), max_length=120, blank=True)
    subteam = models.CharField(
        _("alt takım"),
        max_length=20,
        choices=SubTeam.choices,
        default=SubTeam.MECHANICAL,
        db_index=True,
    )
    bio = models.TextField(_("kısa biyografi"), blank=True)
    photo = models.ImageField(_("fotoğraf"), upload_to="team/", blank=True)

    instagram_url = models.URLField(_("Instagram"), blank=True)
    linkedin_url = models.URLField(_("LinkedIn"), blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = _("Üye")
        verbose_name_plural = _("Üyeler")

    def __str__(self):
        return self.name
