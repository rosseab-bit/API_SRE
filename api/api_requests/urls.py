from django.urls import path
from . import views
urlpatterns = [
    path("getdata", views.getData, name="getdata"),
]