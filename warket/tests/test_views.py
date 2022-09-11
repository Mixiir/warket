from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("list_wines")
        # self.detail_url = reverse("detail_wine", args=['wine.id'])
        # self.manufacturer = Manufacturer.objects.create(
        #     name="manufacturer",
        #     country="EE",
        #     region="EE",
        #     bio="bio",
        # )
        # self.wine = Wine.objects.create(
        #     id=1,
        #     name="wine1",
        #     description="wine1 description",
        #     rating=1,
        #     vintage=1999,
        #     alchohol_content=12.5,
        #     price_per_unit=10.0,
        #     units_in_stock=10,
        #     type="red",
        #     user=1,
        #     manufacturer="manufacturer",
        # )

    def test_wine_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "list_wines.html")

# def test_wines_detail_GET(self):
#     response = self.client.get(self.detail_url)
#
#     self.assertEquals(response.status_code, 200)
#     self.assertTemplateUsed(response, "detail_wine.html")
