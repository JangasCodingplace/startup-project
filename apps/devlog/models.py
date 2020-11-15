from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from assets.helper import generate_key


class Version(models.Model):
    version = models.CharField(
        _("Version"),
        max_length=11,
        primary_key=True,
        help_text="Format MAJ.MIN.PATCH"
    )

    class Meta:
        verbose_name = _("Version")
        verbose_name_plural = _("Versions")
        ordering = ("-version", )

    def __str__(self):
        return f"v{self.version}"

    def save(self, *args, **kwargs):
        self.version_validation()
        super().save(*args, **kwargs)

    def version_validation(self):
        """
        Raises Error if version has wrong format
        """
        versions = self.version.split('.')
        if len(versions) != 3:
            raise ValidationError("Fromat needs to be MAJ.MIN.PATCH")
        for v in versions:
            int(v)

    @property
    def patchcount(self):
        return self.patches.count()


class Patch(models.Model):
    key = models.CharField(
        _("Key"),
        max_length=6,
        primary_key=True,
        editable=False
    )
    description = models.TextField(
        _("Description")
    )
    timestamp = models.DateTimeField(
        _("Timestamp"),
        auto_now_add=True
    )
    version = models.ForeignKey(
        Version,
        on_delete=models.PROTECT,
        related_name="patches",
        verbose_name="Version"
    )

    class Meta:
        verbose_name = _('Patch')
        verbose_name_plural = _('Patches')
        ordering = ('-timestamp', )

    def __str__(self):
        if len(self.description) < 43:
            return self.description
        return f"{self.description[:40]}..."

    def save(self, *args, **kwargs):
        if not self.pk:
            self.key = generate_key(length=6, model=Patch)
        super().save(*args, **kwargs)


class Commit(models.Model):
    commit_url = models.URLField(
        _("Commit"),
        max_length=256,
        primary_key=True,
        help_text="URL of Commit at Github."
    )
    timestamp = models.DateTimeField(
        _("Timestamp"),
        auto_now_add=True
    )
    patch = models.ForeignKey(
        Patch,
        on_delete=models.PROTECT,
        related_name="commits",
        verbose_name=_("Patch")
    )
    version = models.ForeignKey(
        Version,
        on_delete=models.PROTECT,
        related_name="commits",
        verbose_name=_("Version"),
        editable=False
    )

    class Meta:
        verbose_name = _('Commit')
        verbose_name_plural = _('Commits')
        ordering = ('-timestamp', )

    def __str__(self):
        return self.commit_url

    def save(self, *args, **kwargs):
        self.version = self.patch.version
        super().save(*args, **kwargs)
