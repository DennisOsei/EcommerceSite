from django.shortcuts import render

def store_index(request):
	return render(request, 'store/store_index.html', {})

def store_cart(request):
	return render(request, 'store/store_cart.html', {})

def store_checkout(request):
	return render(request, 'store/store_checkout.html', {})
