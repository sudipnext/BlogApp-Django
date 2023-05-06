from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="home"),
    path("add-post", views.add_post, name="add-post"),
]