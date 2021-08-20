from django.urls import path
from . import views

urlpatterns=[
    path("", views.store_index, name="store_index"),
    path("cart/", views.store_cart, name="store_cart"),
    path("checkout/", views.store_checkout, name="store_checkout"),
    path("update_item/", views.update_item, name="update_item"),
    path("process_order/", views.processOrder, name="process_order"),

]