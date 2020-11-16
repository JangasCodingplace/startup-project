from django.urls import path
from . import views


urlpatterns = [
    path(
        '<int:key_pk>',
        views.KeyView.as_view(),
        name="KeyView"
    )
]
