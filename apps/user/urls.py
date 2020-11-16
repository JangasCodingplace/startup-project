from django.urls import path, include


urlpatterns = [
    path('user/', include('user.user.urls')),
    path('auth/', include('user.auth.urls')),
    path('key/', include('user.keys.urls')),
]
