from django.urls import path
from . import views

urlpatterns = [
    path("register-vendor/", views.register_user, name="register-vendor"),
]
