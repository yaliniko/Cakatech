# Deployment & Gelecek Ayarlar

## PythonAnywhere'e Deployment

> `KULLANICI` yerine kendi PythonAnywhere kullanıcı adınızı yazın.

### 1. Kodu yükle

Kodu GitHub'a push'layıp PythonAnywhere **Bash konsolunda** klonlayın:

```bash
git clone https://github.com/KULLANICI/cakatech-site.git
cd cakatech-site
```

(veya "Files" sekmesinden yükleyin.)

### 2. Sanal ortam + bağımlılıklar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. .env oluştur (üretim)

`cp .env.example .env` ve şunları ayarlayın:

```
SECRET_KEY=<yeni-üretilmiş-anahtar>
DEBUG=False
ALLOWED_HOSTS=KULLANICI.pythonanywhere.com
CSRF_TRUSTED_ORIGINS=https://KULLANICI.pythonanywhere.com
ADMIN_URL=cakatech-yonetim/        # tahmin edilmesi zor bir şeyle değiştirin
```

### 4. DB, statik, çeviri, yönetici

```bash
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 5. Web uygulamasını tanımla (Web sekmesi)

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
6. **Reload** butonuna basın.

Site: `https://KULLANICI.pythonanywhere.com/`

### 6. Güncelleme (yeni sürüm)

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

## İngilizce'yi Açmak (ileride)

1. `config/settings.py` → `LANGUAGES` listesinde `("en", "English")` satırını aç.
2. `config/urls.py` → `prefix_default_language=True` yap (URL'ler `/tr/`, `/en/` olur).
3. `python manage.py compilemessages` (EN çevirileri `locale/en/` içinde hazır).
4. Admin'de her içeriğin İngilizce alanlarını (EN sekmesi) doldur.

Dil değiştirici header'da otomatik görünür hale gelir.
