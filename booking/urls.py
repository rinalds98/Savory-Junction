from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('reservations.html', views.BookingList.as_view(), name='reservations'),
    path('menu.html', views.MenuView.as_view(), name='menu'),
]
