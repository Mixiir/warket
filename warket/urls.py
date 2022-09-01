from auctions import views as auctions_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from users import views as user_views
from warket_viewer.views import (WineListView,
                                 DetailWine,
                                 create_wine,
                                 EditWine,
                                 ManufacturersListView,
                                 DetailManufacturer,
                                 CreateManufacturer,
                                 UpdateManufacturer,
                                 DeleteManufacturer,
                                 WineSortedList
                                 )

urlpatterns = [
    path('admin/', admin.site.urls),

    path("cart/", include("cart.urls", namespace="cart")),

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

    path("auctions/", auctions_views.index, name="index"),
    path("auctions/createListing", auctions_views.createListing, name="createListing"),
    path("auctions/details/<int:id>", auctions_views.details, name="details"),
    path("auctions/categories", auctions_views.categories, name="categories"),
    path("auctions/filter/<str:name>", auctions_views.filter, name="filter"),
    path("auctions/comment/<int:id>", auctions_views.comment, name="comment"),
    path("auctions/bid/<int:id>", auctions_views.bid, name="bid"),
    path("auctions/end/<int:item_id>", auctions_views.end, name="end"),
    path("auctions/all", auctions_views.all, name="all"),

]

urlpatterns += staticfiles_urlpatterns()
