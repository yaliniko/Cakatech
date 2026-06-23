"""Çakatech sitesi URL yapılandırması.

- Admin paneli gizli/değiştirilebilir bir yolda (settings.ADMIN_URL).
- Tüm site sayfaları i18n_patterns ile /tr/ ve /en/ önekli.
- set_language: dil değiştirici formunun gönderildiği yerleşik view.
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Dil önekiyle SARILMAYAN yollar (admin, dil değiştirme)
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),  # set_language view'i
]

# Dil önekiyle (/tr/, /en/) sarılan site sayfaları
urlpatterns += i18n_patterns(
    path("", include("apps.core.urls")),
    path("", include("apps.team.urls")),
    path("", include("apps.competitions.urls")),
    path("", include("apps.sponsors.urls")),
    path("", include("apps.contact.urls")),
    # Şimdilik tek dil (TR) → temiz URL'ler (/ , /takim/). İngilizce açılınca
    # bunu True yapın ki varsayılan dil de /tr/ önekiyle gelsin.
    prefix_default_language=False,
)

# Geliştirmede medya dosyalarını servis et (prod'da web sunucusu yapar)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin paneli başlıkları
admin.site.site_header = "Çakatech Yönetim"
admin.site.site_title = "Çakatech Yönetim"
admin.site.index_title = "İçerik Yönetimi"
