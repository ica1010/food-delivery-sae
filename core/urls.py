from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from core.views import *

urlpatterns = [
    path('', Home , name='Home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', Signup, name='signup'),
    path("log-out/", logout_view , name="log-out"),
    path('order_menu/', commande_menu, name='order_menu'),
    path('order_plat/', commande_plat, name='order_plat'),
    path('search/', search, name='search'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit-profile/', Edit_profile, name='edit'),
]