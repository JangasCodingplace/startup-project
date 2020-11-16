from django.http import Http404
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import SetPasswordForm
from user.keys.views import BaseKeyView


class PasswordResetView(PasswordChangeView, BaseKeyView):
    form_class = SetPasswordForm
    template_name = 'user/user/resetPassword.html'
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
