from django.shortcuts import redirect
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Booking, TABLES_AVAILABLE, Review
from .forms import ReviewForm
from datetime import datetime


class IndexView(TemplateView):
    """
    This class renders index.html. It also adds
    reviews to the homepage.
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Gets reviews and initialises form.
        review = super().get_context_data(**kwargs)
        review["reviews"] = Review.objects.all()
        review["review_form"] = ReviewForm()
        return review

    def post(self, request, *args, **kwargs):
        # Checks if the user can post a review and if so posts it.
        form = ReviewForm(request.POST)

        if form.is_valid():
            if Review.objects.filter(user_name=request.user).exists():
                messages.warning(request, "You have already made a review")
                return redirect("home")

            review = form.save(commit=False)
            review.user_name = request.user
            review.save()
            return redirect("home")
        else:
            review = self.get_context_data(**kwargs)
            review["review_form"] = form
            return self.render_to_response(review)


class BookingList(CreateView):
    """
    This class renders the reservation.html page. It takes care of
    creating a reservation for the user.
    """
    # Initiliases the template and fields.
    model = Booking
    fields = ["day", "time"]
    template_name = "reservations.html"
    success_url = reverse_lazy("bookings")

    def get_form(self, form_class=None):
        # initialises form and adds an ID to the day field.
        form = super().get_form(form_class)
        form.fields["day"].widget.attrs.update(
            {"id": "datepicker", "class": "text-center"}
        )
        return form

    def form_valid(self, form):
        # Gets user data
        form.instance.user = self.request.user
        user = form.instance.user
        day = form.cleaned_data["day"]
        time = form.cleaned_data["time"]

        # Checks if booking already exists for user and time
        if Booking.objects.filter(user, day, time).exists():
            messages.warning(
                self.request, "You have already booked a table at this time."
            )
            return self.form_invalid(form)

        # Takes table data.
        booked_tables = Booking.objects.filter(day, time).values_list(
            "table_number", flat=True
        )

        # Checks if the restaurant is fully booked. If not assigns table.
        if len(TABLES_AVAILABLE) == len(booked_tables):
            messages.warning(
                self.request, "Sorry, all tables are booked for this time."
            )
            return self.form_invalid(form)
        else:
            for table in TABLES_AVAILABLE:
                if table[0] not in booked_tables:
                    form.instance.table_number = table[0]
                    break
            form.instance.time_ordered = datetime.now()
            messages.success(self.request, "Booking successfully Made.")
            return super().form_valid(form)


class Reservations(ListView):
    """
    This class is responsible for showing a list of bookings
    the user has created.
    """
    model = Booking
    template_name = "mybookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        # Gets user data
        return Booking.objects.filter(user=self.request.user).order_by(
            "day",
            "time",
        )


class BookingDelete(DeleteView):
    """
    This class removes a users booking from the database.
    """
    model = Booking
    success_url = reverse_lazy("bookings")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Booking deleted successfully.")
        return super().delete(request, *args, **kwargs)


class BookingUpdate(UpdateView):
    """
    This class renders the updatebooking.html page. It takes care of
    updating a reservation for the user. It also checks if the user
    has already booked the specific date or if the restaurant is full.
    """
    model = Booking
    fields = ["day", "time"]
    template_name = "updatebooking.html"
    success_url = reverse_lazy("bookings")

    def get_form(self, form_class=None):
        # initialises form and adds an ID to the day field.
        form = super().get_form(form_class)
        form.fields["day"].widget.attrs.update(
            {"id": "datepicker", "class": "text-center"}
        )
        return form

    def get_context_data(self, **kwargs):
        # Get user data
        context = super().get_context_data(**kwargs)
        context["booking_id"] = self.kwargs["pk"]
        return context

    def form_valid(self, form):
        # Checks if booking already exists for user and time
        user = self.request.user
        day = form.cleaned_data["day"]
        time = form.cleaned_data["time"]

        if Booking.objects.filter(user, day, time).exists():
            messages.warning(
                self.request, "You have already booked a table at this time."
            )
            return self.form_invalid(form)

        # Takes data In
        booked_tables = Booking.objects.filter(day, time).values_list(
            "table_number", flat=True
        )

        # Checks if the restaurant is fully booked. If not assigns table.
        if len(TABLES_AVAILABLE) == len(booked_tables):
            messages.warning(
                self.request, "Sorry, all tables are booked for this time."
            )
            return self.form_invalid(form)
        else:
            for table in TABLES_AVAILABLE:
                if table[0] not in booked_tables:
                    form.instance.table_number = table[0]
                    break
            form.instance.time_ordered = datetime.now()
            messages.success(self.request, "Booking successfully Updated.")
            return super().form_valid(form)
