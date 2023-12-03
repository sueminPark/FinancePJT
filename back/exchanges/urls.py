from django.urls import path
from . import views

urlpatterns = [
    path('get_exchange/', views.get_exchange),
    path('cal_exchange/<str:selected1>/<str:selected2>/', views.cal_exchange),
    
]