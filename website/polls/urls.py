from django.urls import path
from . import views

# /polls/*

urlpatterns = [
    path("", views.index, name="index",),  # /polls/
    path("testing", views.testing, name="testing"),  # /polls/testing
]
