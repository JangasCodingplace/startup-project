from django.urls import path
from . import views
from . import ajax

urlpatterns = [
    path(
        '<int:key_pk>',
        views.KeyView.as_view(),
        name="userKeyKeyView"
    ),
    path(
        'create-key',
        ajax.CreateKeyAPI.as_view(),
        name="userKeyCreateKeyAPI"
    ),
]
