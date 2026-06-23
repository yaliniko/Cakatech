"""
Çakatech FTC takım sitesi — Django ayarları.

Ayarlar ortam değişkenlerinden (.env) okunur (django-environ). Gizli/ortama
özgü değerler (SECRET_KEY, DEBUG, ALLOWED_HOSTS, ADMIN_URL ...) koda gömülmez.
"""

from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Ortam değişkenleri -----------------------------------------------------
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ["127.0.0.1", "localhost"]),
    ADMIN_URL=(str, "cakatech-yonetim/"),
    EMAIL_ENABLED=(bool, False),
    CSRF_TRUSTED_ORIGINS=(list, []),
)

# .env dosyası varsa oku (yoksa sadece gerçek ortam değişkenleri kullanılır)
env_file = BASE_DIR / ".env"
if env_file.exists():
    env.read_env(env_file)

SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-dev-only-change-me-in-production-please-0000",
)
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS")

# Gizli admin yolu (örn. "cakatech-yonetim/"). Sonda / olmalı.
ADMIN_URL = env("ADMIN_URL")

# --- Uygulamalar ------------------------------------------------------------
INSTALLED_APPS = [
    # modeltranslation, admin'den ÖNCE gelmeli ki çevrili alanlar admin'e otursun
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Yerel uygulamalar
    "apps.core",
    "apps.team",
    "apps.competitions",
    "apps.sponsors",
    "apps.contact",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise: statik dosyaları herhangi bir sunucuda servis edebilmek için
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # LocaleMiddleware, SessionMiddleware ile CommonMiddleware arasında olmalı
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Site geneli ayarlar (logo, iletişim, sosyal) her şablonda
                "apps.core.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# --- Veritabanı -------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- Parola doğrulayıcılar --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Uluslararasılaştırma (i18n) --------------------------------------------
LANGUAGE_CODE = "tr"

# Şimdilik yalnız Türkçe. İleride İngilizce'yi açmak için ("en", "English")
# satırını geri ekleyip config/urls.py'de prefix_default_language=True yapmak yeterli.
LANGUAGES = [
    ("tr", "Türkçe"),
    # ("en", "English"),
]

# modeltranslation: varsayılan dil ve çevrili olmayan içeriğe geri dönüş
MODELTRANSLATION_DEFAULT_LANGUAGE = "tr"
MODELTRANSLATION_LANGUAGES = ("tr", "en")
MODELTRANSLATION_FALLBACK_LANGUAGES = ("tr", "en")

LOCALE_PATHS = [BASE_DIR / "locale"]

TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_TZ = True

# --- Statik & Medya ---------------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# WhiteNoise ile sıkıştırılmış + hash'li statik dosya servisi (prod)
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- E-posta ----------------------------------------------------------------
# Formlar şimdilik yalnızca DB'ye kaydeder. EMAIL_ENABLED=True olduğunda
# (profesyonel hosting'e geçişte) bildirim e-postaları gönderilir.
EMAIL_ENABLED = env("EMAIL_ENABLED")
if EMAIL_ENABLED:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env("EMAIL_HOST", default="")
    EMAIL_PORT = env.int("EMAIL_PORT", default=587)
    EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
    EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
    DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default=EMAIL_HOST_USER)
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Form bildirimleri bu adrese gider (EMAIL_ENABLED True ise)
CONTACT_NOTIFY_EMAIL = env("CONTACT_NOTIFY_EMAIL", default="")

# --- Güvenlik (prod) --------------------------------------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    X_FRAME_OPTIONS = "DENY"
