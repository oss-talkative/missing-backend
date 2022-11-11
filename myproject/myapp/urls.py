from django.urls import path, include
from .views import HelloAPI, PostAPI, GetAPI

urlpatterns=[
    path("hello/", HelloAPI),
    path("postApi/", PostAPI),
    path("getApi/", GetAPI),

]