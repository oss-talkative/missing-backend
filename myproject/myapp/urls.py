from django.urls import path, include
from .views import HelloAPI, API

urlpatterns=[
    path("hello/", HelloAPI),
    path("", API),
]