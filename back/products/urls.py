from django.urls import path
from . import views

urlpatterns = [
    path("get_deposit/", views.get_deposit),
    path("get_saving/", views.get_saving),
    path("get_all/", views.get_all),
    path("detail/<str:fin_prdt_nm>/", views.detail),
    path("cart/<str:username>/", views.get_cart),
    path("cart/<str:username>/<str:fin_prdt_nm>/", views.cart),
]