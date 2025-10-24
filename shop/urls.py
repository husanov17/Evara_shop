from django.urls import path
from shop.views import dashboard, detail, LoginUserView, logout_user, ProfileUserView, shop_page, get_products_with_category, register_user, add_to_cart, get_cart_page, del_cart_item, ChangePasswordView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('detail/', detail, name="detail"),

    path('login/', LoginUserView.as_view(), name="login_user"),
    path('logout/', logout_user, name="logout_user"),
    path('profile/', ProfileUserView.as_view(), name="profile"),
    path('register/', register_user, name="register_user"),
    path('change-password/', ChangePasswordView.as_view(), name="change_password"),

    path('shop/', shop_page, name="shop"),
    path('category/<int:category_id>/', get_products_with_category, name="category_products"),

    # cart
    path('cart/add/<int:product_id>/', add_to_cart),
    path('cart/', get_cart_page, name="cart_page"),
    path('remove/<int:product_id>/', del_cart_item, name="remove_cart_item"),

]
