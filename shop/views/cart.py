from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.template.context_processors import request
from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if not cart:
            cart = self.session['session_key']={}

        self.cart = cart

    def add(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id] += 1
        else:
            self.cart[product_id] = 1

        self.session.modified = True

    def remove(self, product_id):
        if str(product_id) in self.cart.keys():
            del self.cart[str(product_id)] 
            self.session.modified = True
            return True
        return False

    def get_quantity(self):
        return len(self.cart.keys())

    def get_product(self):
        products = []

        for pid, quantity in self.cart.items():
            pd = Product.objects.get(id=pid)

            if pd.discount>0:
                total = pd.discount_price*quantity
            else:
                total = pd.price*quantity

            product = {
                "quantity": quantity,
                "data": Product.objects.get(id=pid),
                "total": total,
            }
            products.append(product)
        
        return products

def add_to_cart(request, product_id):
    cart = Cart(request)

    if Product.objects.filter(id=product_id).exists():  
        cart.add(product_id)

    return JsonResponse({"message": "Savatga qo'shildi", "cart_count": cart.get_quantity()})


def get_cart_page(request):
    cart = Cart(request)

    products = cart.get_product()

    data = {
        "path": "Savatcha",
        "cart_count": cart.get_quantity(),
        "products": products
    }

    return render(request, "shop/cart.html", context=data) 


def del_cart_item(request, product_id):
    cart = Cart(request)

    if cart.remove(product_id):
        return redirect("cart_page")

    products = cart.get_product()

    data = {
        "path": "Savatcha",
        "cart_count": cart.get_quantity(),
        "products": products
    }

    return render(request, "shop/cart.html", context=data) 