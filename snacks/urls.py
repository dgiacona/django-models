from django.urls import path
from .views import SnacksListView, SnackDetailView

urlpatterns = [
    path("list/", SnacksListView.as_view(), name="snack_list"),
    path("", include("snacks.urls"))
]