# Çakatech FTC Takım Sitesi — Uygulama Planı

## Genel Bakış

Çakatech FTC robotik takımı için sıfırdan, çift dilli (TR/EN), içeriği admin
panelinden yönetilebilen tanıtım sitesi.

**Kararlar:**
- **Stack:** Django 5.2 LTS + saf HTML/CSS/JS (framework yok), SQLite (başlangıç).
- **Çift dil içerik:** `django-modeltranslation` (model alanlarına otomatik
  `_tr`/`_en`). Arayüz metinleri için Django yerleşik i18n (`gettext` + `.po/.mo`).
- **CMS kapsamı:** Dinamik listeler (üye/yarışma/sponsor) **ve** sayfa metin
  blokları (başlık/paragraf) admin'den düzenlenebilir.
- **Formlar:** İletişim ve "Sponsor Ol" formları **şimdilik yalnızca DB'ye**
  kaydedilir. E-posta `EMAIL_ENABLED` bayrağıyla hazır ama kapalı; profesyonel
  hosting'e geçişte açılacak.
- **Tasarım:** Hazır logo + marka renkleri kullanılır. CSS, renkleri tek yerden
  giydirmek için değişken (CSS custom properties) tabanlı.
- **Deployment:** PythonAnywhere (başta ücretsiz tier'a uygun).

> **NOT:** "Robot & Projeler" sayfası kaldırıldı. Site artık **5 sayfa**.

---

## Bağımlılıklar

- `Django` (5.2 LTS)
- `django-modeltranslation` — çift dil model alanları
- `Pillow` — ImageField (logo, üye foto, sponsor logosu)
- `django-environ` — ayarları ortam değişkeninden okuma
- `whitenoise` — statik dosya servisi (taşınabilirlik)

---

## Proje Yapısı

```
cakatech-site/
├─ manage.py
├─ requirements.txt
├─ .env.example            # örnek ortam değişkenleri (.env gitignore)
├─ .gitignore
├─ Understand.md           # mimari + kurulum + deployment dokümanı
├─ config/                 # proje paketi (settings, urls, wsgi)
├─ locale/                 # .po/.mo (arayüz çevirileri)
├─ static/                 # css/main.css, js/main.js, img/ (logo)
├─ media/                  # yüklenen görseller (gitignore)
├─ templates/              # base.html + sayfa şablonları
└─ apps/
   ├─ core/         # SiteSettings, PageContent, Ana Sayfa, base şablon, context processor
   ├─ team/         # Member (Takım & Üyeler)
   ├─ competitions/ # Competition, Achievement (Yarışmalar & Başarılar)
   ├─ sponsors/     # Sponsor (liste) + SponsorshipInquiry (Sponsor Ol formu)
   └─ contact/      # ContactMessage (İletişim formu)
```

---

## 5 Sayfa ↔ App / Model

| Sayfa | URL (TR) | App | İçerik |
|---|---|---|---|
| Ana Sayfa | `/tr/` | core | PageContent blokları + öne çıkanlar (başarılar, sponsorlar) |
| Takım & Üyeler | `/tr/takim/` | team | `Member` listesi + PageContent intro |
| Yarışmalar & Başarılar | `/tr/yarismalar/` | competitions | `Competition` + `Achievement` |
| Sponsor Ol | `/tr/sponsor/` | sponsors | `Sponsor` listesi + `SponsorshipInquiry` formu |
| İletişim | `/tr/iletisim/` | contact | `SiteSettings` iletişim + `ContactMessage` formu |

EN tarafında slug'lar çevrilir (`/en/team/`, `/en/competitions/` …).

---

## Veri Modelleri (`*` = TR/EN çevrilen alan)

- **core.SiteSettings** (singleton): site_name, tagline*, about_short*, logo,
  favicon, email, phone, address*, instagram/youtube/linkedin/twitter, footer_text*.
- **core.PageContent**: key (unique), label, title*, body*, image. Migration ile
  tohumlanır; editör mevcut blokları düzenler.
- **team.Member**: name, role*, subteam (kaptan/mentor/mekanik/yazılım/tasarım/
  medya/iş-geliştirme), bio*, photo, sosyal linkler, order, is_active.
- **competitions.Competition**: name*, season, date, location*, description*,
  result*, image, order, is_active.
- **competitions.Achievement**: title*, description*, date, image, order, is_active.
- **sponsors.Sponsor**: name, logo, url, tier (platin/altın/gümüş/bronz/partner),
  description*, order, is_active.
- **sponsors.SponsorshipInquiry**: name, organization, email, phone, message,
  created_at, is_read. (form → sadece DB)
- **contact.ContactMessage**: name, email, phone, subject, message, created_at,
  is_read. (form → sadece DB)

Ortak soyut base'ler: `OrderedModel` (order + is_active), `TimeStampedModel`
(created_at + updated_at) — `apps/core/models.py`.

---

## Çift Dil (i18n)

- `LANGUAGE_CODE='tr'`, `LANGUAGES=[('tr','Türkçe'),('en','English')]`,
  `LocaleMiddleware`, `i18n_patterns` → tüm sayfalar `/tr/` ve `/en/` önekli.
- Arayüz metinleri: `{% trans %}` + `makemessages`/`compilemessages`.
- DB içeriği: modeltranslation, aktif dile göre otomatik döner.
- Dil değiştirici: header'da `set_language` view'i.

---

## CMS / Admin

- **Gizli admin URL:** `ADMIN_URL` env'den (örn. `cakatech-yonetim/`).
- **2 rol (Groups, data migration):**
  - **Admin:** tüm içerik + kullanıcı yönetimi + SiteSettings.
  - **Editor:** içerik modelleri (üye, yarışma, sponsor, PageContent, mesajlar);
    kullanıcı/ayar yetkisi yok. `is_staff=True`.
- `TranslationAdmin` → çevrili alanlar TR/EN sekmeli.
- Mesaj modelleri: salt-okunur gelen kutusu (is_read + okundu işaretle aksiyonu).
- Form spam koruması: honeypot gizli alan.

---

## Front-end

- `templates/base.html`: header (logo + nav + dil değiştirici) + footer
  (iletişim/sosyal, context processor ile her sayfada).
- `static/css/main.css`: CSS değişkenli (koyu tema + kırmızı/sarı vurgu — logoya
  uygun), mobile-first responsive.
- `static/js/main.js`: mobil menü toggle.

---

## Ayarlar & Deployment

- `config/settings.py` env tabanlı (`django-environ`): SECRET_KEY, DEBUG,
  ALLOWED_HOSTS, ADMIN_URL, EMAIL_*.
- Prod: DEBUG=False, WhiteNoise ile statik, MEDIA web sunucusundan.
- PythonAnywhere: venv + pip install, WSGI, env, `migrate`, `collectstatic`,
  `compilemessages`, `createsuperuser`, static/media mapping.

---

## Uygulama Sırası

1. İskelet: proje + config + env + .gitignore + requirements + git init.
2. i18n + base şablon + nav + dil değiştirici + CSS iskeleti.
3. core: SiteSettings + PageContent + context processor + Ana Sayfa.
4. İçerik app'leri: team, competitions, sponsors + translation + admin + sayfalar + seed.
5. Formlar: ContactMessage & SponsorshipInquiry (sadece DB) + honeypot.
6. Admin sertleştirme: gizli URL + 2 rol (data migration).
7. Tasarım giydirme: logo/renkler, responsive cila, demo içerik.
8. Doküman (Understand.md) + deployment.

---

## Doğrulama

- `runserver` → 5 sayfa `/tr/` ve `/en/` altında gezilir, içerik+arayüz doğru dilde.
- Gizli admin'de Admin/Editor giriş → izinler doğru.
- Formlar gönderilince admin'de kayıt görünür; honeypot çalışır.
- TR↔EN geçişi içerik+menüyü çevirir.
- Mobil (≈375px) responsive + menü toggle.
- `manage.py check`, temel testler, `collectstatic`.
