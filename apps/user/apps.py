
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = _('User')

    def ready(self):
        from . import user
        from . import keys
