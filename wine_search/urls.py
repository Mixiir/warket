from . import views
from django.urls import path

app_name = 'wine_search'

urlpatterns = [
    path('', views.searchapi, name='wine_search'),
    ]
