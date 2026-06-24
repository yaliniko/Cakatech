# Yerel Kurulum

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
