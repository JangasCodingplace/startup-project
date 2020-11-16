from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from .models import Key
from django.views.generic import View


class KeyView(View):
    def get_key(self, key_pk):
        key = get_object_or_404(Key, key=key_pk)
        if not key.is_valid:
            raise Http404("Key is expired.")

    def activation(self, request, key):
        user = key.user
        user.is_activated_by_key = True
        user.save()
        return redirect("indexIndex")

    def get(self, request, key_pk, *args, **kwargs):
        key = self.get_key(key_pk)
        if key.function == "a":
            return self.activation(request, key)
        return redirect("indexIndex")
