from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import View
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Key


class BaseKeyView:
    def authentication(self, request, user):
        login(request, user)

    def get_key_authentication(self, request, key_pk):
        key = get_object_or_404(Key, key=key_pk)
        if not key.is_valid:
            key.delete()
            raise Http404("Key is expired.")
        self.authentication(request, key.user)
        return key


class KeyView(View, BaseKeyView):

    def activation(self, request):
        user = request.user
        user.is_activated_by_key = True
        user.save()
        return redirect("indexIndex")

    def get(self, request, key_pk, *args, **kwargs):
        key = self.get_key_authentication(request=request, key_pk=key_pk)
        if key.function == "a":
            key.delete()
            return self.activation(request)
        if key.function == "pw":
            return redirect("userPasswordResetView",
                            **{'key_pk': key.key})
        return redirect("indexIndex")
