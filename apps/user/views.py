from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import AuthenticationForm, RegistrationForm
from django.urls import reverse


class SignInView(LoginView):
    http_method_names = ["post", ]
    form_class = AuthenticationForm
    template_name = 'staticPages/index.html'


class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'staticPages/index.html'
    success_url = "/"
