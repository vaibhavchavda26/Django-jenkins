from django.urls import path
from django_jenkins import views as dj_views

urlpatterns = [
    path("", dj_views.hello, name="hello")
]
