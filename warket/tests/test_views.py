from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from warket_viewer.models import Manufacturer, Wine
from auctions.models import AuctionListing, Bid, Comment, Category
from users.models import MyUser


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("list_wines")
        self.detail_url = reverse("detail_wine", args=[1])
        self.user = MyUser.objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
            birth_date="1999-01-01",
            is_active=True,
            is_staff=True,
            is_superuser=True,
            date_joined=timezone.now(),
            image="default.jpg",
            country="EE",
            bio="random text",
            language="EE",
            seller=True,
            buyer=True,
            auctioneer=True,
            auction_limit=99999,
            sold_wines=0,
            bought_wines=0,
            auctioned_wines_bought=0,
            auctioned_wines_sold=0,
        )
        self.manufacturer = Manufacturer.objects.create(
            name="Test Random Manufacturer",
            country="EE",
            region="EE",
            bio="random text",
        )
        self.wine = Wine.objects.create(
            name="Test Wine",
            image="default.jpg",
            thumbnail="default.jpg",
            description="Test wine description",
            rating=1,
            vintage=1999,
            alcohol_content=12.5,
            price_per_unit=10.0,
            units_in_stock=10,
            manufacturer=self.manufacturer,
            type="red",
            user=self.user,
        )
        self.category = Category.objects.create(
            name="Test Category",
        )
        self.auction_listing = AuctionListing.objects.create(
            category=self.category,
            name="Test Auction Listing",
            description="Test auction listing description",
            date=timezone.now(),
            start_bid=10.0,
            user=self.user,
            image_url="default.jpg",
            image="default.jpg",
            auction_period=1,
            end_date=timezone.now() + timezone.timedelta(days=1),
            active=True,
        )

    def test_wine_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "list_wines.html")

    def test_wines_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "detail_wine.html")

    def test_manufacturer_detail_GET(self):
        response = self.client.get(reverse("detail_manufacturer", args=[1]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "detail_manufacturer.html")

    def test_create_wine_POST(self):
        response = self.client.post(reverse("create_wine"), {
            "name": "Test Wine",
            "image": "default.jpg",
            "thumbnail": "default.jpg",
            "description": "Test wine description",
            "rating": 1,
            "vintage": 1999,
            "alcohol_content": 12.5,
            "price_per_unit": 10.0,
            "units_in_stock": 10,
            "manufacturer": self.manufacturer,
            "type": "red",
            "user": self.user,
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Wine.objects.count(), 1)
        self.assertEquals(MyUser.objects.count(), 1)
        self.assertEquals(Manufacturer.objects.count(), 1)
        self.assertEquals(Wine.objects.last().name, "Test Wine")

    def test_create_manufacturer_POST(self):
        response = self.client.post(reverse("create_manufacturer"), {
            "name": "Test Manufacturer",
            "country": "EE",
            "region": "EE",
            "bio": "random text",
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Manufacturer.objects.count(), 2)
        self.assertEquals(
            Manufacturer.objects.first().name,
            "Test Random Manufacturer"
        )
        self.assertEquals(Manufacturer.objects.last().name, "Test Manufacturer")

    def test_update_wine_POST(self):
        response = self.client.post(reverse("edit_wine", args=[1]), {
            "name": "Test Wine1",
            "image": "default.jpg",
            "thumbnail": "default.jpg",
            "description": "Test wine",
            "rating": 1.0,
            "vintage": 1999,
            "alcohol_content": 12.5,
            "price_per_unit": 10,
            "units_in_stock": 10,
            "units_in_auction": 0,
            "type": "Red",
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Wine.objects.count(), 1)
        self.assertEquals(Wine.objects.first().name, "Test Wine1")

    def test_auction_listing_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "list_wines.html")
        self.assertEquals(
            AuctionListing.objects.first().name,
            "Test Auction Listing"
        )

    def test_auction_listing_detail_GET(self):
        response = self.client.get(reverse("details", args=[1]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "auctions/details.html")
        self.assertEquals(AuctionListing.objects.count(), 1)
        self.assertEquals(
            AuctionListing.objects.first().name,
            "Test Auction Listing"
        )

    def test_create_auction_listing_POST(self):
        response = self.client.post(reverse("create_listing"), {
            "name": "Test Auction Listing",
            "category": self.category,
            "start_bid": 12,
            "description": "Test auction listing description",
            "user": self.user,
            "comments_allowed": True,
            "auction_period": 1,
        })
        # print(response.context["form"].errors)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(AuctionListing.objects.count(), 1)
        self.assertEquals(AuctionListing.objects.last().name,
                          "Test Auction Listing")

    def test_wine_delete_POST(self):
        response = self.client.post(reverse(
            "delete_wine",
            args=[1]),
            follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Wine.objects.count(), 0)

    def test_manufacturer_delete_POST(self):
        response = self.client.post(reverse(
            "delete_manufacturer",
            args=[1]),
            follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Manufacturer.objects.count(), 0)

