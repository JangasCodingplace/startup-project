from django.contrib.auth.views import LoginView
from .forms import AuthenticationForm


class SignInView(LoginView):
    http_method_names = ["post", ]
    form_class = AuthenticationForm
