from .cart import Cart

def nav_cart(request):
	return {'cart':Cart(request)}