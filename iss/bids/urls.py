from django.urls import path

from iss.bids import views

app_name = "bids"

urlpatterns = [
    path("list/", views.item_list_view, name="item_list"),
    path("detail/<str:pk>/", views.item_detail_view, name="item_detail"),
    path("add/", views.item_create_view, name="item_add"),
    path("update/<str:pk>/", views.item_update_view, name="item_update"),
    path("delete/<str:pk>/", views.item_delete_view, name="item_delete"),

    # TODO: add a way to create and view bids in a list way (no need to create detail view)
    # path("bid_list", views.bid_list_view, name="bid_list"),
    # path("bid/detail/<str:pk>/", views.bid_detail_view, name="bid_detail"),
    # path("bid_add/", views.bid_create_view, name="bid_add"),
]
