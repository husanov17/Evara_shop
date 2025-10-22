from django.urls import path
from shop.views import dashboard, detail, accounts, compare, login_register, shop_page, get_products_with_category
from shop.views import  wishilst, profile_user, login_user, logout_user, register_user, shop_page, get_cart_page
from shop.views.cart import add_to_cart, del_cart_item
from shop.views.user import cart_

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('detail/', detail, name="detail"),

    path('accounts/', accounts, name="accounts"),
    path('cart/', cart_, name="cart"),
    path('compare/', compare, name="compare"),
    path('login_register/', login_register, name="login_register"),
    path('shop/', shop_page, name="shop"),
    path('category/<int:category_id>/', get_products_with_category, name="category_products"),
    path('whishlist/', wishilst, name="whishilst"),
    path('profile/', profile_user, name="profile"),
    path('register/', register_user, name="register_user"),


    path('login/', login_user, name="login_user"),  
    path('logout/', logout_user, name="logout_user"),

    # cart
    path('cart/add/<int:product_id>/', add_to_cart),
    path('cart/', get_cart_page, name="cart_page"),
    path('remove/', del_cart_item, name="remove cart item")   
]