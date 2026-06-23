"""sponsors URL'leri."""

from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = "sponsors"

urlpatterns = [
    path(_("sponsor/"), views.sponsor_page, name="page"),
]
