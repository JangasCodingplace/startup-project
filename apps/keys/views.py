from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login
from .models import Key
from django.views.generic import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import SetPasswordForm


class KeyView(View):
    def get_key(self, key_pk):
        key = get_object_or_404(Key, key=key_pk)
        if not key.is_valid:
            key.delete()
            raise Http404("Key is expired.")
        key.delete()
        return key

    def authentication(self, request, user):
        login(request, user)

    def activation(self, request, key):
        user = key.user
        user.is_activated_by_key = True
        user.save()
        self.authentication(request, user)
        return redirect("indexIndex")

    def get(self, request, key_pk, *args, **kwargs):
        key = self.get_key(key_pk)
        if key.function == "a":
            return self.activation(request, key)
        return redirect("indexIndex")


class ResetPWView(PasswordChangeView):
    form_class = SetPasswordForm
