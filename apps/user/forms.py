from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, password_validation
from django.core.exceptions import ValidationError

from keys.models import Key
from .models import User


class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    error_messages = {
        'invalid_login': _(
            "Please enter a correct email and password."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user = authenticate(self.request, email=email,
                                     password=password)
            if self.user is None or self.user.is_activated_by_key:
                raise self.get_invalid_login_error()
        return self.cleaned_data

    def get_user(self):
        return self.user

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login'
        )


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(required=True)

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', )

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class KeyForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, request=None, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.instance = instance

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def create_key(self):
        email = self.cleaned_data.get('email')
        self.user = self.get_user(email=email)

    def clean(self):
        self.create_key()

    def save(self):
        if self.user is not None:
            self.instance = Key.objects.create(user=self.user)
        return self.instance
