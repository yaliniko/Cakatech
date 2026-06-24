# Çakatech FTC Takım Sitesi

FTC robotik takımı **Çakatech** için Django tabanlı tanıtım sitesi.

- Yerel kurulum → [setup.md](setup.md)
- PythonAnywhere deployment → [deploy.md](deploy.md)

---

## Genel Bakış

- **Stack:** Django 5.2 + saf HTML/CSS/JS (framework yok), SQLite.
- **Dil:** Şu an **yalnız Türkçe** (temiz URL'ler: `/`, `/takim/` …).
  Çift dil altyapısı (modeltranslation + i18n) hazır; İngilizce sonradan tek
  ayarla açılır (bkz. deploy.md §İngilizce).
- **CMS:** Gizli URL'li Django admin; içerik (üye, yarışma, sponsor, sayfa
  metinleri) panelden yönetilir.
- **Formlar:** İletişim & Sponsor Ol → **şimdilik yalnız DB'ye** kaydeder.
- **Tamamlanan sayfa:** Ana Sayfa. Diğer 4 sayfa şu an "Yakında" placeholder'ı.

---

## Proje Yapısı

```
config/            Django proje paketi (settings, urls, wsgi)
apps/
  core/            SiteSettings (singleton), PageContent, Ana Sayfa, base şablon,
                   context processor, paylaşılan model/form/bildirim yardımcıları
  team/            Member (Takım & Üyeler)            — sayfa placeholder
  competitions/    Competition, Achievement           — sayfa placeholder
  sponsors/        Sponsor + SponsorshipInquiry formu — sayfa placeholder
  contact/         ContactMessage formu               — sayfa placeholder
templates/         base.html + sayfa şablonları + partials/coming_soon.html
static/            css/main.css (logo renkleri), js/main.js, img/logo.jpg
locale/            tr & en çevirileri (.po/.mo)
media/             admin'den yüklenen görseller (git'e girmez)
.env               ortam değişkenleri (git'e girmez; .env.example'dan kopyalanır)
```

**Önemli kod noktaları**
- `config/settings.py` — django-environ ile env tabanlı ayar; `LANGUAGES` (TR),
  `ADMIN_URL`, `EMAIL_ENABLED`, WhiteNoise statik storage.
- `config/urls.py` — gizli admin yolu + `i18n_patterns(prefix_default_language=False)`.
- `apps/core/models.py` — `OrderedModel`, `TimeStampedModel`, `SiteSettings`, `PageContent`.
- `apps/core/context_processors.py` — `site` (SiteSettings) ve `blocks` (key→PageContent)
  her şablona enjekte edilir.
- `apps/core/migrations/0002_seed_content.py` — başlangıç içeriği (site ayarları + Ana Sayfa blokları).
- `apps/core/migrations/0003_roles.py` — **Yönetici** ve **Editör** yetki grupları.

---

## İçerik Yönetimi (Admin)

Admin paneline gizli URL'den (`.env`'deki `ADMIN_URL`) girilir.

- **Site Ayarları** — logo, favicon, slogan, kısa tanıtım, iletişim (e-posta/
  telefon/adres), sosyal medya, alt bilgi. Tek satırdır (silinemez/eklenemez).
- **Sayfa Metinleri** — Ana Sayfa blokları (`home_hero`, `home_about`). Editör
  metni değiştirir; anahtar (key) sabittir.
- **Üyeler / Yarışmalar / Başarılar / Sponsorlar** — liste içerikleri; `sıra`
  ve `aktif` alanlarıyla sıralama/gizleme.
- **İletişim Mesajları / Sponsorluk Başvuruları** — formlardan gelen kayıtlar;
  salt-okunur gelen kutusu, "okundu" işaretleme.

**Roller (yetki grupları):**
- **Yönetici** — her şey (içerik + kullanıcı yönetimi + site ayarları).
- **Editör** — yalnız içerik modelleri; kullanıcı yönetimi ve site ayarları yok.

Yeni personel: admin'den kullanıcı oluştur → "personel durumu" (is_staff) işaretle
→ **Yönetici** veya **Editör** grubuna ekle.
