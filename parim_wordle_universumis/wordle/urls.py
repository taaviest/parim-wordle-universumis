from django.urls import path
from . import views

urlpatterns = {
    path("", views.pealeht, name="pealeht"),
}