from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart
    
    def add(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] += 1
        else:
            self.cart[product_id] = 1
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
            return True
        return False

    def get_count(self):
        return len(self.cart.keys())

    def get_products(self):
        products = []
        total_with_discount = 0

        for pid, quantity in self.cart.items():
            pd = Product.objects.get(id=pid)
            if pd.discount > 0:
                total = pd.discount_price * quantity
            else:
                total = pd.price * quantity
            
            total_with_discount += total

            product = {
                "quantity": quantity,
                "data": pd,
                "total": total
            }
            products.append(product)

        total_price = sum(p['data'].price * p['quantity'] for p in products)
        return {
            "products": products,
            "total_price": total_price,
            "total_with_discount": total_with_discount,
            "profit": total_price - total_with_discount
        }

    def clear(self):
        self.cart.clear()
        self.session.modified = True
