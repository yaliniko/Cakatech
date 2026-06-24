# System Patterns

## Mimari

```
config/          → Django proje paketi (settings, urls, wsgi)
apps/core/       → SiteSettings singleton, PageContent, Ana Sayfa, context processor
apps/team/       → Member modeli
apps/competitions/ → Competition, Achievement modelleri
apps/sponsors/   → Sponsor, SponsorshipInquiry modelleri
apps/contact/    → ContactMessage modeli
templates/       → base.html + sayfa şablonları
static/          → CSS, JS, görseller
  static/css/main.css  → Glassmorphism dark tema, CSS custom properties
  static/js/main.js    → IntersectionObserver, mobile hamburger
  static/img/logo.jpg  → Marka logosu (hareketsiz)
locale/          → .po/.mo çeviri dosyaları
memory-bank/     → Proje belleği (bu klasör)
```

## Temel Desenler

### Singleton Model (SiteSettings)
`apps/core/models.py` — `save()` her zaman `pk=1` yazar, `load()` classmethod ile çekilir. Tek satır, silinemez.

### PageContent (Sayfa Metin Blokları)
`key` alanıyla şablonlara enjekte edilir. `context_processors.py` → `blocks` dict'i her şablonda mevcut. Bloklar `0002_seed_content.py` migration'ıyla tohumlanır.

### Context Processor
`apps/core/context_processors.py` → `site` (SiteSettings) ve `blocks` (key→PageContent) her şablona otomatik enjekte edilir.

### Soyut Base Modeller
- `OrderedModel` → `order` + `is_active` alanları
- `TimeStampedModel` → `created_at` + `updated_at` alanları

### Yetki Rolleri (Groups)
`0003_roles.py` migration ile oluşturulur:
- **Yönetici** → tüm izinler
- **Editör** → yalnız içerik modelleri

### i18n
- `i18n_patterns(prefix_default_language=False)` → TR için temiz URL (`/`, `/takim/`)
- `modeltranslation` → model alanları TR/EN çevrili (`_tr`/`_en` suffix)
- Dil değiştirici header'da, yalnız `LANGUAGES` > 1 olduğunda görünür

### Spam Koruması (Formlar)
`HoneypotForm` base class → gizli `website` alanı; dolu gelirse `ValidationError`

### Statik Dosyalar
WhiteNoise `CompressedManifestStaticFilesStorage` → prod'da hash'li, sıkıştırılmış

## Frontend Tasarım Sistemi (2026-06-24 sonrası)

### CSS Custom Properties (`:root`)
- `--brand`: `#e2231a` (kırmızı)
- `--accent`: `#ffd200` (sarı)
- `--bg-deep`, `--bg-mid`, `--bg-surface` → koyu tonlar
- `--border-glass`, `--shadow-glow` → glassmorphism yardımcıları

### Bileşen Sınıfları
- `.glass-panel` → `backdrop-filter: blur` + yarı saydam arka plan
- `.btn-primary` / `.btn-ghost` → ana buton stilleri
- `.hero`, `.section`, `.page-header` → sayfa düzeni yardımcıları
- `.animate-on-scroll` → IntersectionObserver ile tetiklenen fade-in
- `.brand-no` → sarı renkte takım numarası gösterimi (`#25160`)

### Animasyon Politikası
- Sayfa kartları: `animate-on-scroll` (IntersectionObserver)
- Logo: **animasyonsuz** (hover dönme ve hero float kaldırıldı)
- Butonlar/kartlar: hover transform ile hafif yükselme

## Gizli Admin URL
`ADMIN_URL` env değişkeninden okunur → `config/urls.py`'de `path(settings.ADMIN_URL, admin.site.urls)`
