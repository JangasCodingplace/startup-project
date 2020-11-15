
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DevlogConfig(AppConfig):
    name = 'devlog'
    verbose_name = _('Devlog')
