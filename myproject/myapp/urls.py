from django.urls import path, include
from .views import HelloAPI, PostAPI, GetAllAPI, GetNameAPI

urlpatterns=[
    path("hello/", HelloAPI),
    path("postApi/", PostAPI),
    path("getAllApi/", GetAllAPI),
    path("getNameApi/", GetNameAPI),

]