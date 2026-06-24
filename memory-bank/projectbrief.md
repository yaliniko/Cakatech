# Project Brief — Çakatech FTC Takım Sitesi

## Proje Tanımı

FTC (First Tech Challenge) robotik takımı **Çakatech #25160** için Django tabanlı tanıtım sitesi.

## Temel Gereksinimler

- Takımı tanıtan sayfalık web sitesi
- İçerik admin panelinden yönetilebilir (CMS)
- Şimdilik sadece Türkçe; İngilizce altyapısı hazır
- PythonAnywhere'de ücretsiz tier'da çalışacak
- Formlar veritabanına kaydedilir (Sponsor başvurusu)

## Aktif Sayfalar & Navigasyon

| Sayfa | URL | Durum |
|---|---|---|
| Ana Sayfa | `/` | ✅ Tamamlandı |
| Takım & Üyeler | `/takim/` | ✅ Tasarım hazır, içerik boş |
| Yarışmalar & Başarılar | `/yarismalar/` | ✅ Tasarım hazır, içerik boş |
| Sponsor Ol | `/sponsor/` | ✅ Tasarım hazır, içerik boşaltıldı |
| İletişim | `/iletisim/` | ⚠️ Navigasyondan kaldırıldı, backend mevcut |

## Kapsam Dışı (Şimdilik)

- E-posta bildirimleri (ileride profesyonel hosting'de açılacak)
- İngilizce içerik (altyapı hazır, açılmadı)
- Özel admin dashboard
- CI/CD pipeline
