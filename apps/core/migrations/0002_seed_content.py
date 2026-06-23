"""Başlangıç içeriği: SiteSettings (singleton) + Ana Sayfa metin blokları.

Editörler bu blokların metnini admin'den düzenler; bloklar burada tohumlanır.
"""

from django.db import migrations


SITE = {
    "site_name": "Çakatech",
    "tagline_tr": "Geleceği bugünden inşa eden FTC robotik takımı.",
    "tagline_en": "An FTC robotics team building the future today.",
    "about_short_tr": (
        "Çakatech, FIRST Tech Challenge yarışmalarında ülkemizi temsil eden, "
        "tasarımdan yazılıma her şeyi takım olarak üreten genç mühendisler topluluğudur."
    ),
    "about_short_en": (
        "Çakatech is a community of young engineers competing in the FIRST Tech "
        "Challenge — designing, building and coding everything as a team."
    ),
    "email": "info@cakatech.com",
    "footer_text_tr": "Çakatech FTC Robotik Takımı",
    "footer_text_en": "Çakatech FTC Robotics Team",
}

BLOCKS = [
    {
        "key": "home_hero",
        "label": "Ana Sayfa — Hero (büyük başlık)",
        "title_tr": "Çakatech",
        "title_en": "Çakatech",
        "body_tr": "Tasarlıyoruz, kodluyoruz, yarışıyoruz. Robotik tutkusuyla bir araya gelmiş bir takımız.",
        "body_en": "We design, we code, we compete. A team united by a passion for robotics.",
    },
    {
        "key": "home_about",
        "label": "Ana Sayfa — Hakkımızda",
        "title_tr": "Biz Kimiz?",
        "title_en": "Who Are We?",
        "body_tr": (
            "Çakatech olarak FIRST Tech Challenge sezonlarında robot tasarlayıp üretiyor, "
            "yazılım geliştiriyor ve takım ruhuyla yarışıyoruz. Amacımız teknolojiyi üretmek "
            "ve gençleri mühendislikle buluşturmak."
        ),
        "body_en": (
            "At Çakatech we design and build robots for FIRST Tech Challenge seasons, write "
            "software and compete with true team spirit. Our goal is to create technology and "
            "bring young people together with engineering."
        ),
    },
]


def seed(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    PageContent = apps.get_model("core", "PageContent")

    SiteSettings.objects.update_or_create(pk=1, defaults=SITE)

    for block in BLOCKS:
        defaults = {k: v for k, v in block.items() if k != "key"}
        PageContent.objects.update_or_create(key=block["key"], defaults=defaults)


def unseed(apps, schema_editor):
    PageContent = apps.get_model("core", "PageContent")
    PageContent.objects.filter(key__in=[b["key"] for b in BLOCKS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
