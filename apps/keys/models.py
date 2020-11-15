from random import randint
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from assets.choices import KEY_FUNCTIONS


class Key(models.Model):
    key = models.SmallIntegerField(
        _("Key"),
        primary_key=True,
        editable=False
    )
    timestamp = models.DateTimeField(
        _("Timestamp"),
        auto_now_add=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
        related_name="keys"
    )
    function = models.CharField(
        _("Key Function"),
        max_length=2,
        choices=KEY_FUNCTIONS,
        editable=False
    )

    class Meta:
        verbose_name = _("Key")
        verbose_name_plural = _("Keys")

    def __str__(self):
        return str(self.key)

    def save(self, *args, **kwargs):
        self.__set_key()
        self.__set_function()
        super().save(*args, **kwargs)

    def __set_key(self):
        self.key = randint(1000, 9999)
        while Key.objects.filter(key=self.key).exists():
            self.key = randint(1000, 9999)

    def __set_function(self):
        if self.user.is_activated_by_key:
            self.function = "pw"
        else:
            self.function = "a"

    @property
    def is_valid(self):
        """ To Do """
        return True
