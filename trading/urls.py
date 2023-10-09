from django.urls import path
from . import views

urlpatterns = [
    path("admin-view/traders", views.allTraders, name="allTraders"),
    path("admin-view/traders/<str:id>", views.getTrader, name="getTrader"),
    path("login", views.get_trader_login, name="login")
    # path("trader/<str:name>")
]
