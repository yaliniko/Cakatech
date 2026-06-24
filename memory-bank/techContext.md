# Tech Context

## Stack

| Katman | Teknoloji |
|---|---|
| Backend | Django 6.x (PA'da kurulu sürüm) |
| Dil | Python 3.13 |
| Veritabanı | SQLite |
| Statik | WhiteNoise |
| Frontend | Saf HTML/CSS/JS (framework yok) |

## Bağımlılıklar (`requirements.txt`)

- `Django` — web framework
- `django-modeltranslation` — model alanlarına TR/EN çeviri
- `django-environ` — env tabanlı ayarlar
- `Pillow` — ImageField (logo, fotoğraf)
- `whitenoise` — statik dosya servisi

## Geliştirme Ortamı

```bash
cd ~/Programming/Çakatech-site
source .venv/bin/activate
python manage.py runserver
# → http://127.0.0.1:8000/
```

## Deployment (PythonAnywhere)

- Kullanıcı: `yaliniko`
- Dizin: `~/Cakatech` (tire yok!)
- Python: 3.13, venv: `~/Cakatech/.venv`
- WSGI: `/var/www/yaliniko_pythonanywhere_com_wsgi.py`
- Canlı URL: `https://yaliniko.pythonanywhere.com/`

## Ortam Değişkenleri (`.env`)

```
SECRET_KEY=...
DEBUG=False
ALLOWED_HOSTS=yaliniko.pythonanywhere.com          # sadece hostname!
CSRF_TRUSTED_ORIGINS=https://yaliniko.pythonanywhere.com
ADMIN_URL=...                                        # gizli admin yolu
EMAIL_ENABLED=False                                  # e-posta kapalı
```

## Teknik Kısıtlar

- PythonAnywhere ücretsiz tier → dış SMTP kısıtlı (e-posta deferred)
- SQLite → tek sunucu, büyük trafik için yeterli (FTC takımı için OK)
- `media/` → PythonAnywhere'de kalıcı, git'e girmez

## Önemli Komutlar

```bash
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py createsuperuser
python manage.py check --deploy
```
