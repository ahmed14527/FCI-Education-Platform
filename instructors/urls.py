from django.urls import path
from .views import create_superuser

urlpatterns = [
    path('create-docaccount/', create_superuser, name='create_superuser'),
]