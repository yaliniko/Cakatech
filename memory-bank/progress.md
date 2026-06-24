# Progress

## Çalışan / Tamamlanan

- [x] Django proje iskeleti (config, 5 app, migrations)
- [x] Seed migration (SiteSettings + Ana Sayfa blokları)
- [x] Yetki rolleri migration (Yönetici + Editör grupları)
- [x] Honeypot spam koruması
- [x] WhiteNoise statik servis
- [x] PythonAnywhere deployment (canlıda!)
- [x] Doküman: README.md + setup.md + deploy.md
- [x] memory-bank/ oluşturuldu

### Frontend Yenilemesi (2026-06-24)
- [x] `static/css/main.css` — glassmorphism dark theme, CSS custom properties, sade scrollbar
- [x] `static/js/main.js` — IntersectionObserver fade-in, mobile hamburger
- [x] `templates/base.html` — premium navbar, modern footer, mobile menü
- [x] `templates/core/home.html` — hero + 4'lü stat grid (2x2) + başarı kartları + sponsor şeridi + CTA
- [x] `templates/team/team_list.html` — alt takım bazlı üye kartları
- [x] `templates/competitions/competitions_list.html` — timeline + gurur tablosu
- [x] `templates/sponsors/sponsor_page.html` — içerik boşaltıldı (sadece page-header)
- [x] `templates/contact/contact.html` — navigasyondan kaldırıldı (backend mevcut)
- [x] Takım numarası **#25160** tüm kritik noktalara eklendi (navbar, hero, stat kart, footer)
- [x] Logo animasyonları kaldırıldı (navbar dönme efekti + hero float)
- [x] Robot scrollbar kaldırıldı, sade scrollbar eklendi

## Yapılacaklar

- [ ] Admin'den SiteSettings doldurmak (logo, iletişim, sosyal medya)
- [ ] Takım & Üyeler sayfası — gerçek içerik
- [ ] Yarışmalar & Başarılar sayfası — gerçek içerik
- [ ] Sponsor Ol sayfasının içeriğine karar vermek (şu an boş)
- [ ] git init + GitHub push
- [ ] Canlıya (PythonAnywhere) güncel kodu aktarmak + collectstatic

## İleride (Ertelenmiş)

- [ ] İngilizce dil desteği (altyapı hazır, `deploy.md` §İngilizce)
- [ ] Özel admin dashboard

## Bilinen Sorunlar / Notlar

- PythonAnywhere dizin adı `Cakatech` (tire yok, büyük C) — yerel repoda `Çakatech-site`
- `ALLOWED_HOSTS` env değerinde `https://` veya `/` olmamalı (daha önce hata yaptı)
- Django sürümü: `requirements.txt`'te `Django` pin'siz; PA'da 6.0.6 kuruldu
- İletişim sayfası (`/iletisim/`) backend'de aktif; yalnız navbar/footer'dan kaldırıldı
- Büyük CSS değişikliğinden sonra tarayıcıda Ctrl+F5 (hard refresh) gerekebilir
