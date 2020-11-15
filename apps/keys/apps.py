from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class KeysConfig(AppConfig):
    name = 'keys'
    verbose_name = _('Keys')
