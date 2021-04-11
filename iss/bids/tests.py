from datetime import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from iss.bids.models import AuctionedItem, Bid
from iss.users.models import User


class IssUnitTests(TestCase):

    def create_auction_item(self, seller, name="test name", description="test description"):
        return AuctionedItem.objects.create(
            name=name,
            description=description,
            amount=10,
            start_date=datetime.now(),
            end_date=datetime.now(),
            seller=seller
        )

    def test_model_example(self):
        dummy_user = User(username='dummy')
        dummy_user.save()
        auction_item = self.create_auction_item(name="test name change", seller=dummy_user)
        self.assertTrue(isinstance(auction_item, AuctionedItem))
        self.assertEqual(auction_item.name, "test name change")

    def test_view_example(self):
        dummy_user = User(username='dummy')
        dummy_user.save()
        auction_item = self.create_auction_item(name="test name change", seller=dummy_user)

        url = reverse("items:bid_add")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(auction_item.name, "test name change")