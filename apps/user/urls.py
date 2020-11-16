from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('signin', views.SignInView.as_view(), name="userSignInView"),
    path('signup', views.SignUpView.as_view(), name="userSignUpView"),
    path('logout', LogoutView.as_view(), name="userLogoutView"),
    path('create-key', views.CreateKeyView.as_view(), name="userCreateKeyView"),
]
