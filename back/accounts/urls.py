from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    path("<int:user_pk>/", views.detail),
    path("update/<int:user_pk>/", views.update_user),
]