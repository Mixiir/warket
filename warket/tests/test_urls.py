from django.urls import reverse, resolve
from django.test import SimpleTestCase

from warket_viewer.views import (
    WineListView,
    create_wine,
    DetailWine,
    ManufacturersListView,
    DetailManufacturer,
    CreateManufacturer,
    UpdateManufacturer,
    DeleteManufacturer,
    WineSortedList,
    EditWine,
    DeleteWine,
)


class TestUrls(SimpleTestCase):

    def test_list_wine_url_is_resolved(self):
        url = reverse('list_wines')
        self.assertEquals(resolve(url).func.view_class, WineListView)

    def test_create_wine_url_is_resolved(self):
        url = reverse('create_wine')
        self.assertEquals(resolve(url).func, create_wine)

    def test_detail_wine_url_is_resolved(self):
        url = reverse('detail_wine', args=[1])
        self.assertEquals(resolve(url).func.view_class, DetailWine)

    def test_detail_manufacturer_url_is_resolved(self):
        url = reverse('detail_manufacturer', args=[1])
        self.assertEquals(resolve(url).func.view_class, DetailManufacturer)

    def test_create_manufacturer_url_is_resolved(self):
        url = reverse('create_manufacturer')
        self.assertEquals(resolve(url).func.view_class, CreateManufacturer)

    def test_update_manufacturer_url_is_resolved(self):
        url = reverse('update_manufacturer', args=[1])
        self.assertEquals(resolve(url).func.view_class, UpdateManufacturer)

    def test_delete_manufacturer_url_is_resolved(self):
        url = reverse('delete_manufacturer', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteManufacturer)

    def test_delete_wine_url_is_resolved(self):
        url = reverse('delete_wine', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteWine)

    # def test_wine_sorted_list_url_is_resolved(self):
    #     url = reverse('list_wines_sorted', kwargs={'show_only': 'name'})
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, WineSortedList)

    def test_edit_wine_url_is_resolved(self):
        url = reverse('edit_wine', args=[1])
        self.assertEquals(resolve(url).func.view_class, EditWine)

    def test_list_manufacturers_url_is_resolved(self):
        url = reverse('list_manufacturers')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ManufacturersListView )