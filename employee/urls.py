from django.urls import path

from . import views

# Serves the application
urlpatterns = [
    path(route="", view=views.index, name="index"),
]
