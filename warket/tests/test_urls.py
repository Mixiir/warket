from django.urls import reverse, resolve
from django.test import SimpleTestCase

from warket_viewer.views import WineListView, create_wine, DetailWine, ManufacturersListView


class TestUrls(SimpleTestCase):

    #    path("", WineListView.as_view(), name="list_wines"),

    def test_list_wine_url_is_resolved(self):
        url = reverse('list_wines')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, WineListView)

    #    path("create_wine/", create_wine, name="create_wine"),

    def test_create_wine_url_is_resolved(self):
        url = reverse('create_wine')
        print(resolve(url))
        self.assertEquals(resolve(url).func, create_wine)

#    path("manufacturers/", ManufacturersListView.as_view(), name="list_manufacturers"),

    def test_list_manufacturers_url_is_resolved(self):
        url = reverse('list_manufacturers')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ManufacturersListView )
