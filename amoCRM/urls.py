from django.urls import path
from .views import GetAuth, ContactView

urlpatterns = [
    path('auth_code', GetAuth.as_view()),
    path('contacts/', ContactView.as_view())
]