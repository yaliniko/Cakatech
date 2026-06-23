"""Yarışma ve başarı modelleri."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import OrderedModel


class Competition(OrderedModel):
    """Katılınan bir yarışma (Yarışmalar & Başarılar sayfası)."""

    name = models.CharField(_("yarışma adı"), max_length=160)
    season = models.CharField(_("sezon"), max_length=40, blank=True)
    date = models.DateField(_("tarih"), null=True, blank=True)
    location = models.CharField(_("yer"), max_length=160, blank=True)
    description = models.TextField(_("açıklama"), blank=True)
    result = models.CharField(
        _("sonuç / derece"), max_length=160, blank=True,
        help_text=_("Örn. Bölge 3.'lüğü, Finalist"),
    )
    image = models.ImageField(_("görsel"), upload_to="competitions/", blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = _("Yarışma")
        verbose_name_plural = _("Yarışmalar")

    def __str__(self):
        return self.name


class Achievement(OrderedModel):
    """Kazanılan bir ödül / başarı."""

    title = models.CharField(_("başlık"), max_length=160)
    description = models.TextField(_("açıklama"), blank=True)
    date = models.DateField(_("tarih"), null=True, blank=True)
    image = models.ImageField(_("görsel / ikon"), upload_to="achievements/", blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = _("Başarı")
        verbose_name_plural = _("Başarılar")

    def __str__(self):
        return self.title
