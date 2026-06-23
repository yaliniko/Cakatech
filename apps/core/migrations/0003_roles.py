"""İki yetki rolü (grubu) oluşturur: 'Yönetici' (Admin) ve 'Editör'.

- Yönetici: tüm yetkiler (içerik + kullanıcı/grup + site ayarları).
- Editör: yalnız içerik modelleri (üye, yarışma, başarı, sponsor, başvuru,
  mesaj, sayfa metni). Kullanıcı yönetimi ve site ayarlarına erişemez.

Personel kullanıcılar admin'den bu gruplara eklenir.
"""

from django.apps import apps as global_apps
from django.contrib.auth.management import create_permissions
from django.db import migrations

# Editörün yönetebileceği içerik modelleri (app_label, model_adı)
EDITOR_MODELS = [
    ("team", "member"),
    ("competitions", "competition"),
    ("competitions", "achievement"),
    ("sponsors", "sponsor"),
    ("sponsors", "sponsorshipinquiry"),
    ("contact", "contactmessage"),
    ("core", "pagecontent"),
]


def setup_roles(apps, schema_editor):
    # İzinlerin bu migration anında mevcut olmasını garanti et
    for app_config in global_apps.get_app_configs():
        create_permissions(app_config, verbosity=0)

    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    # --- Yönetici: tüm izinler ---
    admin_group, _ = Group.objects.get_or_create(name="Yönetici")
    admin_group.permissions.set(Permission.objects.all())

    # --- Editör: yalnız içerik modelleri ---
    editor_group, _ = Group.objects.get_or_create(name="Editör")
    editor_perms = Permission.objects.filter(
        content_type__app_label__in={a for a, _ in EDITOR_MODELS},
        content_type__model__in={m for _, m in EDITOR_MODELS},
    )
    # app_label + model çiftini tam eşleştir (yukarıdaki filtre kombinasyonları geniş tutar)
    allowed = set(EDITOR_MODELS)
    editor_group.permissions.set(
        [p for p in editor_perms if (p.content_type.app_label, p.content_type.model) in allowed]
    )


def remove_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["Yönetici", "Editör"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_seed_content"),
        ("team", "0001_initial"),
        ("competitions", "0001_initial"),
        ("sponsors", "0001_initial"),
        ("contact", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(setup_roles, remove_roles),
    ]
