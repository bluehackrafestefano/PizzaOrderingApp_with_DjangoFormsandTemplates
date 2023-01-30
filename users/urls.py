from django.urls import path, include
from .views import register


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]