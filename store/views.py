from django.shortcuts import render
from .models import *


def store_index(request):
	products = Product.objects.all()
	context = {"products": products}
	return render(request, 'store/store_index.html', context)

def store_cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		# create empty cart
		items = []
		order = {"get_cart_total": 0, "get_cart_items": 0}

	context = {"items": items, "order": order}
	return render(request, 'store/store_cart.html', context)

def store_checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		order = {"get_cart_total": 0, "get_cart_items": 0}
		items = []

	context = {"items": items, "order": order}
	return render(request, "store/store_checkout.html", context)
	
    
