from django.urls import path
from .views import addFoundChild, allFoundChild, nameFoundChild, FoundChild

urlpatterns=[
    path("addFoundChild/", addFoundChild),
    path("allFoundChild/", allFoundChild),
    path("nameFoundChild/", nameFoundChild),
    path("FoundChild/", FoundChild),

]