from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from iss.bids.models import Bid, AuctionedItem
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404


class ItemDetailView(DetailView):
    model = AuctionedItem
    context_object_name = "item"
    template_name = "items/item_detail.html"
    slug_field = "item"
    slug_url_kwarg = "item_id"


item_detail_view = ItemDetailView.as_view()


class ItemListView(ListView):
    model = AuctionedItem
    paginate_by = 10
    context_object_name = "item_list"
    template_name = "items/item_list.html"


item_list_view = ItemListView.as_view()


class ItemCreateView(CreateView):
    model = AuctionedItem
    fields = ["name", "description", "amount", "start_date", "end_date"]
    template_name = "items/item_form.html"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


item_create_view = ItemCreateView.as_view()


class ItemUpdateView(UpdateView):
    model = AuctionedItem
    fields = ["name", "description", "amount", "start_date", "end_date"]
    template_name = "items/item_form.html"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


item_update_view = ItemUpdateView.as_view()


class ItemDeleteView(DeleteView):
    model = AuctionedItem
    template_name = "items/item_form.html"
    success_url = reverse_lazy("home")


item_delete_view = ItemDeleteView.as_view()


class BidDetailView(DetailView):
    model = Bid
    template_name = "bids/bid_detail.html"
    slug_field = "bid"
    slug_url_kwarg = "bid_id"


bid_detail_view = BidDetailView.as_view()


class BidListView(ListView):
    paginate_by = 10
    context_object_name = "bid_list"
    template_name = "bids/bid_list.html"

    def get_queryset(self):
        return Bid.objects.filter(item__pk=self.kwargs["pk"])


bid_list_view = BidListView.as_view()


class BidCreateView(CreateView):
    model = Bid

    # 'bidder' and 'item' should be filled automatically
    fields = ["amount"]
    template_name = "bids/bid_form.html"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


bid_create_view = BidCreateView.as_view()


class BidUpdateView(UpdateView):
    model = Bid

    # 'bidder' and 'item' should be filled automatically
    fields = ["amount"]
    template_name = "bids/bid_form.html"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


bid_update_view = BidUpdateView.as_view()


class BidDeleteView(DeleteView):
    model = Bid
    template_name = "bids/bid_form.html"
    success_url = reverse_lazy("home")


bid_delete_view = BidDeleteView.as_view()
