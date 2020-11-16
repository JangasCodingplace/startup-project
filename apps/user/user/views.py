from django.http import Http404
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView
from .forms import AuthenticationForm, KeyForm
from django.contrib.auth.forms import SetPasswordForm
from keys.views import BaseKeyView


class SignInView(LoginView):
    http_method_names = ["post", ]
    form_class = AuthenticationForm


class CreateKeyView(CreateView):
    form_class = KeyForm
    success_url = "/"


class PasswordResetView(PasswordChangeView, BaseKeyView):
    form_class = SetPasswordForm
    template_name = 'user/resetPassword.html'
    success_url = "/"

    def key_validation(self, request, key_pk):
        key = self.get_key_authentication(request=request, key_pk=key_pk)
        if key.function != "pw":
            raise Http404("Invalid Key.")
        return key

    def get(self, request, key_pk, *args, **kwargs):
        self.key_validation(request, key_pk)
        return self.render_to_response({'key_pk': key_pk})

    def post(self, request, key_pk, *args, **kwargs):
        key = self.key_validation(request, key_pk)
        key.delete()
        return super().post(request, *args, **kwargs)
