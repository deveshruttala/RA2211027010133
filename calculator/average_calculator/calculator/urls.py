from django.urls import path
from .views import fetch_and_calculate

urlpatterns = [
    path('numbers/<str:numberid>/', fetch_and_calculate),
]