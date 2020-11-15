from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Key


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_key_by_registration(*args, **kwargs):
    if kwargs['created']:
        Key.objects.create(user=kwargs['instance'])
