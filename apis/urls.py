from django.urls import path
from . import views

urlpatterns =  [
    path("",views.BookApiListView.as_view(), name="listbook")
]