from django.shortcuts import render
from django.urls import reverse_lazy

from iss.bids.models import Bid, AuctionedItem


class ItemDetailView(DetailView):
    model = AuctionedItem
    template_name = "items/item_detail.html"
    slug_field = "item"
    slug_url_kwarg = "item_id"


item_detail_view = ItemDetailView.as_view()


class ItemListView(ListView):
    model = AuctionedItem
    paginate_by = 10
    template_name = "items/item_list.html"

    # # def get_queryset(self):
    # #     tag = self.request.GET.get("tag", None)
    # #     if tag:
    # #         base_queryset = A.objects.filter(
    # #             Q(tags__name__in=[tag]),
    # #             Q(is_approved=True),
    # #             Q(publish_date__lte=datetime.now()),
    # #             # Has no expiration date or has not expired yet
    # #             Q(expiration_date__isnull=True)
    # #             | Q(expiration_date__gte=datetime.now()),
    # #         )
    # #     else:
    # #         base_queryset = Article.objects.filter(
    # #             Q(is_approved=True),
    # #             Q(publish_date__lte=datetime.now()),
    # #             # Has no expiration date or has not expired yet
    # #             Q(expiration_date__isnull=True)
    # #             | Q(expiration_date__gte=datetime.now()),
    # #         )

    # #     sort = self.request.GET.get("sort", None)
    # #     if sort == "title":
    # #         base_queryset = base_queryset.order_by("title")
    # #     elif sort == "publish_date":
    # #         base_queryset = base_queryset.order_by("publish_date")
    # #     elif sort == "expiration_date":
    # #         base_queryset = base_queryset.order_by("expiration_date")
    # #     return base_queryset

    # def get_ordering(self):
    #     ordering = self.request.GET.get("ordering", "-publish_date")
    #     return ordering


item_list_view = ItemListView.as_view()


class ItemCreateView(CreateView):
    model = AuctionedItem
    fields = [
        "name",
        "description",
        "amount",
        "start_date",
        "end_date"
    ]
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


item_create_view = ItemCreateView.as_view()


class ItemUpdateView(UpdateView):
    model = AuctionedItem
    fields = [
        "name",
        "description",
        "amount",
        "start_date",
        "end_date"
    ]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


item_update_view = ItemUpdateView.as_view()


class ItemDeleteView(ArticleUserPassesTestMixin, DeleteView):
    model = AuctionedItem
    success_url = reverse_lazy("items:list")


item_delete_view = ItemDeleteView.as_view()



# class BidDetailView(DetailView):
#     model = Bid
#     template_name = "bids/bid_detail.html"
#     slug_field = "bid"
#     slug_url_kwarg = "bid_id"


# bid_detail_view = BidDetailView.as_view()


# class BidListView(ListView):
#     model = Bid
#     paginate_by = 10
#     template_name = "bids/bid_list.html"

#     # # def get_queryset(self):
#     # #     tag = self.request.GET.get("tag", None)
#     # #     if tag:
#     # #         base_queryset = A.objects.filter(
#     # #             Q(tags__name__in=[tag]),
#     # #             Q(is_approved=True),
#     # #             Q(publish_date__lte=datetime.now()),
#     # #             # Has no expiration date or has not expired yet
#     # #             Q(expiration_date__isnull=True)
#     # #             | Q(expiration_date__gte=datetime.now()),
#     # #         )
#     # #     else:
#     # #         base_queryset = Article.objects.filter(
#     # #             Q(is_approved=True),
#     # #             Q(publish_date__lte=datetime.now()),
#     # #             # Has no expiration date or has not expired yet
#     # #             Q(expiration_date__isnull=True)
#     # #             | Q(expiration_date__gte=datetime.now()),
#     # #         )

#     # #     sort = self.request.GET.get("sort", None)
#     # #     if sort == "title":
#     # #         base_queryset = base_queryset.order_by("title")
#     # #     elif sort == "publish_date":
#     # #         base_queryset = base_queryset.order_by("publish_date")
#     # #     elif sort == "expiration_date":
#     # #         base_queryset = base_queryset.order_by("expiration_date")
#     # #     return base_queryset

#     # def get_ordering(self):
#     #     ordering = self.request.GET.get("ordering", "-publish_date")
#     #     return ordering


# bid_list_view = BidListView.as_view()


# class BidCreateView(ArticleUserPassesTestMixin, CreateView):
#     model = Bid
#     fields = [
#         # "title",
#         # "content",
#         # "short_description",
#         # "publish_date",
#         # "expiration_date",
#     ]

#     def form_valid(self, form):
#         # form.instance.author = self.request.user
#         # form.instance.is_approved = False

#         return super().form_valid(form)


# bid_create_view = BidCreateView.as_view()
