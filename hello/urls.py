from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.saludo, name="saludo"),
    path("fernando", views.fernando, name="fernando"),
    path("david", views.david, name="david")
]

