"""warket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from warket_viewer.views import WineListView, RegisterUser, DetailWine, CreateWine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WineListView.as_view(), name="list_wines"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('wine/<int:pk>', DetailWine.as_view(), name="detail_wine"),
    path('create_wine/', CreateWine.as_view(), name="create_wine"),

]
