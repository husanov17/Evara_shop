from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.context_processors import request
from shop.models import Product
from shop.utils import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)

    if Product.objects.filter(id=product_id).exists():
        cart.add(product_id)

    return JsonResponse({"message": "Savatga qo'shildi", "cart_count": cart.get_count()})


def get_cart_page(request):
    cart = Cart(request)

    products = cart.get_products()

    data = {
        'path': "Savatcha",
        "cart_count": cart.get_count(),
        "products": products
    }
    return render(request, "shop/cart.html", context=data)


def del_cart_item(request, product_id):
    cart = Cart(request)

    if cart.remove(product_id):
        return redirect("cart_page")

    products = cart.get_products()

    data = {
        'path': "Savatcha",
        "cart_count": cart.get_count(),
        "products": products
    }
    return render(request, "shop/cart.html", context=data)

    
