from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.HomePage, name="home"),
    path("list",views.BookListView.as_view(), name="list")
]