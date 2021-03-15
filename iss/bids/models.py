from django.db import models
from django.contrib.auth import get_user_model


class AuctionedItem(models.Model):
    name = models.TextField(
        null=False,
        blank=False,
        help_text='numele obiectului'
    )
    description = models.TextField(
        null=False,
        blank=False,
        help_text='descrierea obiectului'
    )
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=False,
        blank=False,
        help_text='cine pune la licitatie obiectul'
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="pretul curent al licitatiei"
    )
    start_date = models.DateTimeField(
        help_text='data cand incepe licitatia'
    )
    end_date = models.DateTimeField(
        help_text='data cand se termina licitatia'
    )


class Bid(models.Model):
    bidder = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=False,
        blank=False,
        help_text='cine face o oferta'
    )
    item = models.ForeignKey(
        AuctionedItem,
        on_delete=models.SET_NULL,
        null=False,
        blank=False,
        help_text='licitatia'
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="cat ofera"
    )
