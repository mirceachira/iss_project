from django.contrib import admin

from iss.bids import models

admin.site.register(models.AuctionedItem)
admin.site.register(models.Bid)
