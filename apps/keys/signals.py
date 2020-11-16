import threading
import os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils.html import strip_tags
from .models import Key


class EmailThread(threading.Thread):
    sender_mail = os.getenv("SENDER_MAIL")
    base_url = os.getenv("URL")
    subject = None
    message = None

    def __init__(self, key):
        self.key = key
        threading.Thread.__init__(self)

    def get_context(self):
        return {"key": self.key, "base_url": self.base_url}

    def get_message(self, template):
        raw_message = get_template(template)
        message = raw_message.render(self.get_context())
        return message

    def set_subject_and_message_for_activation_mail(self):
        self.subject = "Thanks for registration!"
        self.message = self.get_message("email/activation.html")

    def set_subject_and_message_for_pw_forgotten_mail(self):
        self.subject = "Password forgotten"
        self.message = self.get_message("email/passwordForgotten.html")

    def _send_mail(self):
        send_mail(
            subject=self.subject, message=strip_tags(self.message),
            from_email=self.sender_mail, recipient_list=[self.key.user.email],
            html_message=self.message
        )

    def run(self):
        if self.key.function == "a":
            self.set_subject_and_message_for_activation_mail()
        if self.key.function == "pw":
            self.set_subject_and_message_for_pw_forgotten_mail()
            print("\n\nPW FORGOTTEN\n\n")
        if self.subject and self.message:
            self._send_mail()
            print("\n\nMAIL SENDED\n\n")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_key_by_registration(*args, **kwargs):
    if kwargs['created']:
        Key.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=Key)
def send_key_via_mail(*args, **kwargs):
    if kwargs['created']:
        EmailThread(kwargs['instance']).start()
