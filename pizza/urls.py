from django.urls import path
from .views import home, order, edit_order
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('order/<int:id>/', edit_order, name='edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)