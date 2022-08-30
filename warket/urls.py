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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from warket_viewer.views import (WineListView,
                                 DetailWine,
                                 create_wine,
                                 EditWine,
                                 ManufacturersListView,
                                 DetailManufacturer,
                                 CreateManufacturer,
                                 UpdateManufacturer,
                                 DeleteManufacturer,
                                 CartListView,
                                 AddToCart,
                                 RemoveFromCart,
                                 WineSortedList
                                 )
from users import views as user_views
from auctions import views as auctions_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WineListView.as_view(), name="list_wines"),
    path('', WineSortedList.as_view(), name="list_wines_sorted"),
    path('manufacturers/', ManufacturersListView.as_view(), name="list_manufacturers"),
    path('manufacturer/<int:pk>', DetailManufacturer.as_view(), name='detail_manufacturer'),
    path('create_manufacturer/', CreateManufacturer.as_view(), name='create_manufacturer'),
    path('manufacturer/<int:pk>/delete', DeleteManufacturer.as_view(), name='delete_manufacturer'),
    path('manufacturer/<int:pk>/update', UpdateManufacturer.as_view(), name='update_manufacturer'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('wine/<int:pk>', DetailWine.as_view(), name="detail_wine"),
    path('create_wine/', create_wine, name="create_wine"),
    path('wine/<int:pk>/edit/', EditWine.as_view(), name="edit_wine"),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('add_to_cart/', AddToCart.as_view(), name='add_to_cart'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('remove_from_cart/<int:pk>', RemoveFromCart.as_view(), name='remove_from_cart'),

    path("auctions/", auctions_views.index, name="index"),
    path("auctions/createListing", auctions_views.createListing, name="createListing"),
    path("auctions/details/<int:id>", auctions_views.details, name="details"),
    path("auctions/categories", auctions_views.categories, name="categories"),
    path("auctions/filter/<str:name>", auctions_views.filter, name="filter"),
    path("auctions/comment/<int:id>", auctions_views.comment, name="comment"),
    path("auctions/bid/<int:id>", auctions_views.bid, name="bid"),
    path("auctions/end/<int:itemId>", auctions_views.end, name="end"),
    path("auctions/all", auctions_views.all, name="all"),
    path("auctions/watchlist", auctions_views.watchlist, name="watchlist"),
    path("auctions/watch", auctions_views.watch, name="watch")
]
urlpatterns += staticfiles_urlpatterns()
