"""Çekirdek modeller: paylaşılan soyut base'ler, site ayarları, sayfa metinleri."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """Oluşturma/güncelleme zamanı tutan soyut base."""

    created_at = models.DateTimeField(_("oluşturulma"), auto_now_add=True)
    updated_at = models.DateTimeField(_("güncellenme"), auto_now=True)

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    """Manuel sıralama + aktiflik bayrağı tutan soyut base."""

    order = models.PositiveIntegerField(_("sıra"), default=0, db_index=True)
    is_active = models.BooleanField(_("aktif"), default=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class SiteSettings(models.Model):
    """Tek satırlık (singleton) site geneli ayarlar: logo, iletişim, sosyal."""

    site_name = models.CharField(_("site adı"), max_length=100, default="Çakatech")
    tagline = models.CharField(_("slogan"), max_length=200, blank=True)
    about_short = models.TextField(_("kısa tanıtım"), blank=True)

    logo = models.ImageField(_("logo"), upload_to="site/", blank=True)
    favicon = models.ImageField(_("favicon"), upload_to="site/", blank=True)

    # İletişim
    email = models.EmailField(_("e-posta"), blank=True)
    phone = models.CharField(_("telefon"), max_length=40, blank=True)
    address = models.CharField(_("adres"), max_length=255, blank=True)

    # Sosyal medya
    instagram_url = models.URLField(_("Instagram"), blank=True)
    youtube_url = models.URLField(_("YouTube"), blank=True)
    linkedin_url = models.URLField(_("LinkedIn"), blank=True)
    twitter_url = models.URLField(_("X / Twitter"), blank=True)

    footer_text = models.CharField(_("alt bilgi metni"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("Site Ayarları")
        verbose_name_plural = _("Site Ayarları")

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        # Singleton: her zaman tek satır (pk=1)
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Singleton silinemez
        pass

    @classmethod
    def load(cls):
        """Ayar satırını döndür; yoksa oluştur."""
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj


class PageContent(models.Model):
    """Sayfa metin bloğu (key bazlı). Editörler admin'den düzenler.

    Bloklar bir veri migrasyonuyla önceden tohumlanır; böylece editör boş
    ekrandan key uydurmaz, sadece mevcut blokların metnini değiştirir.
    """

    key = models.SlugField(
        _("anahtar"),
        max_length=80,
        unique=True,
        help_text=_("Şablonda kullanılan benzersiz anahtar (örn. home_hero)."),
    )
    label = models.CharField(
        _("etiket"),
        max_length=120,
        help_text=_("Bu bloğun ne olduğunu açıklayan ad (admin için)."),
    )
    title = models.CharField(_("başlık"), max_length=255, blank=True)
    body = models.TextField(_("metin"), blank=True)
    image = models.ImageField(_("görsel"), upload_to="pages/", blank=True)

    class Meta:
        verbose_name = _("Sayfa Metni")
        verbose_name_plural = _("Sayfa Metinleri")
        ordering = ["key"]

    def __str__(self):
        return self.label or self.key
