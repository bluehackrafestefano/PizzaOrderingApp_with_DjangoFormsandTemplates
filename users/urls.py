from django.urls import path, include


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
]