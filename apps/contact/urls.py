"""contact URL'leri."""

from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = "contact"

urlpatterns = [
    path(_("iletisim/"), views.contact, name="contact"),
]
