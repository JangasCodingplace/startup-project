from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from . import ajax


urlpatterns = [
    path(
        'reset-pw/<int:key_pk>',
        views.PasswordResetView.as_view(),
        name="userPasswordResetView"
    ),
    path(
        'signup',
        ajax.SignupAPI.as_view(),
        name="userSignUpAPI"
    ),
    path(
        'user-is-taken',
        ajax.UserIsTakenView.as_view(),
        name="userUserIsTakenAPI"
    )
]
