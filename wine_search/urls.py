from . import views
from django.urls import path

app_name = "wine_search"

urlpatterns = [
    path("", views.upload_file, name="wine_search"),
    ]
