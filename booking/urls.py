from . import views
from django.urls import path

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path(
        "reservations.html",
        views.BookingList.as_view(),
        name="reservations",
    ),
    path(
        "mybookings.html",
        views.Reservations.as_view(),
        name="bookings",
    ),
    path(
        "delete/<int:pk>/",
        views.BookingDelete.as_view(),
        name="delete_booking",
    ),
    path(
        "updatebooking.html/<int:pk>/update/",
        views.BookingUpdate.as_view(),
        name="update_booking",
    ),
]
