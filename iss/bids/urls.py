from django.urls import path

from iss.bids import views

app_name = "bids"

urlpatterns = [
    path("item_list", views.item_list_view, name="item_list"),
    path("item_detail/<str:pk>/", views.item_detail_view, name="item_detail"),
    path("item_add/", views.item_create_view, name="item_add"),
    path("item_update/<str:pk>/", views.item_update_view, name="item_update"),
    path("item_delete/<str:pk>/", views.item_delete_view, name="item_delete"),

    # path("bid_list", views.bid_list_view, name="bid_list"),
    # path("bid_detail/<str:pk>/", views.bid_detail_view, name="bid_detail"),
    # path("bid_add/", views.bid_create_view, name="bid_add"),
]
