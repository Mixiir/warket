from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

import auctions.views
from auctions import views as auctions_views
from users import views as user_views
from warket_viewer.views import (CreateManufacturer, DeleteManufacturer,
                                 DeleteWine, DetailManufacturer, DetailWine,
                                 EditWine, ManufacturersListView,
                                 UpdateManufacturer, WineListView,
                                 WineSortedList, create_wine, Home, Base, edit_wine, create_manufacturer)

urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "cart/",
        include(
            "cart.urls",
            namespace="cart"
        )
    ),

    path(
        "wine/",
        WineListView.as_view(),
        name="list_wines"
    ),
    path(
        "wine/",
        WineSortedList.as_view(),
        name="list_wines_sorted"
    ),
    path(
        "manufacturers/",
        ManufacturersListView.as_view(),
        name="list_manufacturers"
    ),
    path(
        "manufacturer/<int:pk>",
        DetailManufacturer.as_view(),
        name="detail_manufacturer"
    ),
    path(
        "create_manufacturer/",
        create_manufacturer,
        name="create_manufacturer"
    ),
    path(
        "manufacturer/<int:pk>/delete",
        DeleteManufacturer.as_view(),
        name="delete_manufacturer"
    ),
    path(
        "manufacturer/<int:pk>/update",
        UpdateManufacturer.as_view(),
        name="update_manufacturer"
    ),
    path(
        "accounts/",
        include("django.contrib.auth.urls")
    ),
    path(
        "wine/<int:pk>",
        DetailWine.as_view(),
        name="detail_wine"
    ),
    path(
        "create_wine/",
        create_wine,
        name="create_wine"
    ),
    path(
        "wine/<int:pk>/edit/",
        edit_wine,
        name="edit_wine"
    ),
    path(
        "wine/<int:pk>/delete",
        DeleteWine.as_view(),
        name="delete_wine"),
    path(
        "register/",
        user_views.register,
        name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html"
        ),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="users/logout.html"
        ),
        name="logout"
    ),
    path(
        "profile/",
        user_views.profile,
        name="profile"
    ),

    path(
        "auctions/",
        auctions_views.auction_index,
        name="auction_index"
    ),
    path(
        "auctions/create_listing",
        auctions_views.create_listing,
        name="create_listing"
    ),
    path(
        "auctions/details/<int:wine_id>",
        auctions_views.details,
        name="details"
    ),
    path(
        "auctions/categories",
        auctions_views.categories,
        name="categories"
    ),
    path(
        "auctions/categories/<str:category>",
        auctions_views.filter,
        name="filter"
    ),
    path(
        "auctions/comment/<int:wine_id>",
        auctions_views.comment,
        name="comment"
    ),
    path(
        "auctions/bid/<int:wine_id>",
        auctions_views.bid,
        name="bid"
    ),
    path(
        "auctions/end/<int:wine_id>",
        auctions_views.end,
        name="end"
    ),
    path(
        "auctions/all_auction_listings",
        auctions_views.all_auction_listings,
        name="all_auction_listings"
    ),
    path(
        "auctions/my_auction_listings",
        auctions_views.my_auction_listings,
        name="my_auction_listings"
    ),
    path(
        "auctions/ended_auction_listings",
        auctions_views.ended_auction_listings,
        name="ended_auction_listings"
    ),
    path(
        "auctions/my_ended_auction_listings",
        auctions_views.my_ended_auction_listings,
        name="my_ended_auction_listings"
    ),
    path(
        "auctions/my_won_auction_listings",
        auctions_views.my_won_auction_listings,
        name="my_won_auction_listings"
    ),
    path("auctions/categories/<int:pk>/delete",
         auctions.views.DeleteCategory.as_view(), name="delete_category"),

    path(
        "", Home.as_view(), name="home"),

    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('/images/favicon.ico'))
    ),
    path(
        "base/", Base.as_view(), name="base"),
]

urlpatterns += staticfiles_urlpatterns()
