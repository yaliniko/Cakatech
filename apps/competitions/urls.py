"""competitions URL'leri."""

from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = "competitions"

urlpatterns = [
    path(_("yarismalar/"), views.competitions_list, name="list"),
]
