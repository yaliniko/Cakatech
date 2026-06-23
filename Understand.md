# Çakatech Sitesi — Mimari & Kurulum & Deployment

FTC robotik takımı **Çakatech** için Django tabanlı tanıtım sitesi.
Bu dosya; mimariyi, yerel kurulumu, içerik yönetimini ve PythonAnywhere
deployment'ını tek başına anlatır.

---

## 1. Genel Bakış

- **Stack:** Django 5.2 + saf HTML/CSS/JS (framework yok), SQLite.
- **Dil:** Şu an **yalnız Türkçe** (temiz URL'ler: `/`, `/takim/` …).
  Çift dil altyapısı (modeltranslation + i18n) hazır; İngilizce sonradan tek
  ayarla açılır (bkz. §7).
- **CMS:** Gizli URL'li Django admin; içerik (üye, yarışma, sponsor, sayfa
  metinleri) panelden yönetilir.
- **Formlar:** İletişim & Sponsor Ol → **şimdilik yalnız DB'ye** kaydeder.
- **Tamamlanan sayfa:** Ana Sayfa. Diğer 4 sayfa şu an "Yakında" placeholder'ı.

---

## 2. Proje Yapısı

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

## 3. Yerel Kurulum

```bash
# 1) Sanal ortam
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate

# 2) Bağımlılıklar
pip install -r requirements.txt

# 3) Ortam dosyası
cp .env.example .env
# .env içindeki SECRET_KEY'i üretin:
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
# çıktıyı .env'deki SECRET_KEY'e yapıştırın

# 4) Veritabanı + başlangıç içeriği + roller
python manage.py migrate

# 5) Çevirileri derle (locale/.mo üretir)
python manage.py compilemessages

# 6) Yönetici hesabı
python manage.py createsuperuser

# 7) Çalıştır
python manage.py runserver
```

Site: <http://127.0.0.1:8000/> · Admin: <http://127.0.0.1:8000/cakatech-yonetim/>
(admin yolu `.env`'deki `ADMIN_URL` ile değişir.)

---

## 4. İçerik Yönetimi (Admin)

Admin paneline gizli URL'den (`ADMIN_URL`) girilir.

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

---

## 5. PythonAnywhere'e Deployment

> Aşağıdaki adımlar ücretsiz tier için de geçerlidir. `KULLANICI` yerine kendi
> PythonAnywhere kullanıcı adınızı yazın.

### 5.1 Kodu yükle
- Kodu GitHub'a push'layıp PythonAnywhere **Bash konsolunda** klonlayın:
  ```bash
  git clone https://github.com/KULLANICI/cakatech-site.git
  cd cakatech-site
  ```
  (veya "Files" sekmesinden yükleyin.)

### 5.2 Sanal ortam + bağımlılıklar
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 5.3 .env oluştur (üretim)
`cp .env.example .env` ve şunları ayarlayın:
```
SECRET_KEY=<yeni-üretilmiş-anahtar>
DEBUG=False
ALLOWED_HOSTS=KULLANICI.pythonanywhere.com
CSRF_TRUSTED_ORIGINS=https://KULLANICI.pythonanywhere.com
ADMIN_URL=cakatech-yonetim/        # tahmin edilmesi zor bir şeyle değiştirin
```

### 5.4 DB, statik, çeviri, yönetici
```bash
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 5.5 Web uygulamasını tanımla (Web sekmesi)
1. **Add a new web app** → **Manual configuration** → Python 3.x.
2. **Virtualenv:** `/home/KULLANICI/cakatech-site/.venv`
3. **Source code / Working directory:** `/home/KULLANICI/cakatech-site`
4. **WSGI configuration file**'ı düzenleyin; içeriğini şununla değiştirin:
   ```python
   import os, sys
   path = "/home/KULLANICI/cakatech-site"
   if path not in sys.path:
       sys.path.insert(0, path)
   os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
5. **Static files** eşlemesi:
   - URL `/static/`  →  Directory `/home/KULLANICI/cakatech-site/staticfiles`
   - URL `/media/`   →  Directory `/home/KULLANICI/cakatech-site/media`
   (WhiteNoise de statik servis eder; bu eşleme yine de önerilir.)
6. **Reload** butonuna basın.

Site: `https://KULLANICI.pythonanywhere.com/`

### 5.6 Güncelleme (yeni sürüm)
```bash
cd ~/cakatech-site && git pull
source .venv/bin/activate
pip install -r requirements.txt        # değiştiyse
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages       # çeviri değiştiyse
# Web sekmesi → Reload
```

---

## 6. Formlara E-posta Eklemek (ileride / profesyonel hosting)

Şu an formlar yalnız DB'ye kaydediyor. E-posta bildirimini açmak için `.env`:
```
EMAIL_ENABLED=True
EMAIL_HOST=...            # SMTP sunucusu
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
DEFAULT_FROM_EMAIL=...
CONTACT_NOTIFY_EMAIL=bildirim@cakatech.com
```
Kod değişikliği gerekmez — `apps/core/notifications.py` bayrağı görünce
bildirim gönderir. (Not: PythonAnywhere ücretsiz tier'da dış SMTP kısıtlıdır.)

---

## 7. İngilizce'yi Açmak (ileride)

1. `config/settings.py` → `LANGUAGES` listesinde `("en", "English")` satırını aç.
2. `config/urls.py` → `prefix_default_language=True` yap (URL'ler `/tr/`, `/en/` olur).
3. `python manage.py compilemessages` (EN çevirileri `locale/en/` içinde hazır).
4. Admin'de her içeriğin İngilizce alanlarını (EN sekmesi) doldur.

Dil değiştirici header'da otomatik görünür hale gelir.
```
