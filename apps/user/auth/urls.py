from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path(
        'signin',
        views.SignInView.as_view(),
        name="userAuthSignInView"
    ),
    path(
        'logout',
        LogoutView.as_view(),
        name="userAuthLogoutView"
    )
]
