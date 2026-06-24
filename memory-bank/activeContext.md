# Active Context

## Mevcut Durum (2026-06-24)

Site canlıda: `https://yaliniko.pythonanywhere.com/`

Frontend tamamen yenilendi — glassmorphism dark theme, premium tasarım dili.  
Tüm 5 sayfa artık gerçek tasarımına kavuştu (placeholder yok).

## Bu Konuşmada Yapılan Değişiklikler (2026-06-24)

### Frontend Yenilemesi (Büyük Güncelleme)
- `static/css/main.css` → sıfırdan yeniden yazıldı (glassmorphism, CSS custom properties, animasyonlar)
- `static/js/main.js` → IntersectionObserver (fade-in), mobile hamburger menü
- `templates/base.html` → glassmorphism navbar, mobile menü, modernize footer
- `templates/core/home.html` → canlı hero, 4'lü istatistik grid (2x2), başarı kartları, sponsor şeridi, CTA
- `templates/team/team_list.html` → alt takım bazlı üye kartları
- `templates/competitions/competitions_list.html` → timeline + gurur tablosu
- `templates/sponsors/sponsor_page.html` → sponsorluk kategorileri + form; **form kısmı sonradan boşaltıldı**
- `templates/contact/contact.html` → iletişim bilgileri + form (**navigasyondan kaldırıldı**)
- Google Fonts: *Outfit* eklendi
- Renk paleti: kırmızı `#e2231a` + sarı `#ffd200` takım renkleri

### Takım Numarası Entegrasyonu
- Takım numarası **#25160** şu noktalara eklendi:
  - Navbar brand adının yanına (sarı `brand-no` span)
  - Hero kicker metnine: `FIRST Tech Challenge Takımı #25160`
  - Ana sayfa istatistik kartlarına 4. kart olarak (`#25160 — Takım Numarası`)
  - Footer telif metnine: `Çakatech #25160`

### Navigasyon Değişiklikleri
- **İletişim sayfası** navbar'dan ve footer'dan kaldırıldı (URL hâlâ aktif, navigasyonda yok)
- **Sponsor Ol** sayfası template'i boşaltıldı (sadece page-header kaldı)

### Kaldırılanlar / İptal Edilenler
- Robot scrollbar (robot.png ile özel webkit scrollbar) → temizlendi
  - `static/img/robot.png` silindi
  - CSS'deki robot scrollbar bloğu → sade ince `8px` scrollbar ile değiştirildi
- Logo hover animasyonu (navbar logosu dönme efekti) → kaldırıldı
- Hero logo float/yüzme animasyonu → kaldırıldı

## Sıradaki Adımlar

1. Admin'den **SiteSettings** doldurmak (logo, e-posta, sosyal medya)
2. **Takım & Üyeler** sayfasını gerçek içerikle doldurmak
3. **Yarışmalar & Başarılar** sayfasını doldurmak
4. **Sponsor Ol** sayfasının içeriğine ne geleceğine karar vermek
5. `git init` + GitHub'a push

## Aktif Kararlar / Dikkat Edilecekler

- PythonAnywhere dizin adı `Cakatech` (tire yok, büyük C) — deployment komutlarında dikkat
- `ALLOWED_HOSTS` formatı: sadece hostname, `https://` veya `/` olmadan
- İletişim sayfası backend'de hâlâ mevcut; yalnızca navigasyondan çıkarıldı
- CSS cache buster: `{% static 'css/main.css' %}?v=2` — büyük değişiklik sonrası Ctrl+F5 gerekebilir
