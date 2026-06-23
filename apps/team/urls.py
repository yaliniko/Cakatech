"""team URL'leri."""

from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = "team"

urlpatterns = [
    path(_("takim/"), views.team_list, name="list"),
]
