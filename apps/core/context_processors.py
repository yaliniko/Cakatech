"""Şablonlara site geneli veriyi geçiren context processor'lar."""

from .models import PageContent, SiteSettings


def site_settings(request):
    """Her şablonda `site` (SiteSettings) ve `blocks` (key->PageContent) sağlar.

    `blocks.home_hero.title` gibi şablon erişimi için PageContent'leri key'e göre
    sözlüğe çevirir. Tek sorgu; tüm sitede paylaşılır.
    """
    blocks = {block.key: block for block in PageContent.objects.all()}
    return {
        "site": SiteSettings.load(),
        "blocks": blocks,
    }
