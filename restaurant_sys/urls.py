from django.urls import path
from . import views
urlpatterns = [
    path('hello', views.hello),
    path('view/<restname>', views.restaurant_view),
    path('view/<restname>/buy', views.buy_site),
    path('view/<restname>/order', views.order_handle),
    path('login', views.loginPage),
    path('logout', views.logoutUser),
    path('manage_order', views.manage_order),
    path('manage_order_detail/<order_id>', views.manage_order_detail),
]