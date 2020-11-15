from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Key


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_key_by_registration(*args, **kwargs):
    if kwargs['created']:
        key = Key.objects.create(user=kwargs['instance'])
        send_mail(
            subject="Activation",
            message=str(key.key),
            from_email="janisgoesser92@gmail.com",
            recipient_list=[key.user.email]
        )
