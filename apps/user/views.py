from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import AuthenticationForm, RegistrationForm


class SignInView(LoginView):
    http_method_names = ["post", ]
    form_class = AuthenticationForm


class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = "/"
