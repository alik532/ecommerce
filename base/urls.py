from . import views
from django.urls import URLPattern, path, include

urlpatterns = [
    path('', views.login_page, name='login'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('register', views.register, name='register'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('main', views.main, name='main'),
    path('profile', views.profile, name='profile'),
    path('profile/edit_profile', views.edit_profile, name='edit_profile'),
    path('profile/change_profile', views.change_profile, name='change_profile'),
    path('main/product', views.product, name='product'),
    path('main/add_comment/<str:prod_name>/', views.add_comment, name='add_comment'),
    path('log_out', views.log_out, name='logout'),
    path('main/add_to_cart/<str:prod_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('delete/<str:product>/', views.delete_from_cart, name='delete'),
]