from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('signin', views.SignInView.as_view(), name="userSignInView"),
    path('logout', LogoutView.as_view(), name="userLogoutView"),
]
