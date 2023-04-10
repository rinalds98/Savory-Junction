from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import *
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Booking, TABLES_AVAILABLE, Review
from .forms import ReviewForm
from datetime import datetime


class IndexView(TemplateView):
    # Loads the home page template
    template_name = "index.html"

    # Gets Reviews
    def get_context_data(self, **kwargs):
        review = super().get_context_data(**kwargs)
        review["reviews"] = Review.objects.all()
        review["review_form"] = ReviewForm()
        return review

    # Posts Review
    def post(self, request, *args, **kwargs):
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
    # This view creates a form so the user can create a reservation
    model = Booking
    fields = ["day", "time"]
    template_name = "reservations.html"
    success_url = reverse_lazy("reservations")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["day"].widget.attrs.update(
            {"id": "datepicker", "class": "text-center"}
        )
        return form

    def form_valid(self, form):
        # Assign user to the booking
        form.instance.user = self.request.user

        # Check if booking already exists for user and time
        if Booking.objects.filter(
            user=form.instance.user,
            day=form.cleaned_data["day"],
            time=form.cleaned_data["time"],
        ).exists():
            messages.warning(
                self.request, "You have already booked a table at this time."
            )
            return self.form_invalid(form)

        # Find available table for booking
        available_tables = TABLES_AVAILABLE
        booked_tables = Booking.objects.filter(
            day=form.cleaned_data["day"], time=form.cleaned_data["time"]
        ).values_list("table_number", flat=True)
        for table in available_tables:
            if table[0] not in booked_tables:
                form.instance.table_number = table[0]
                break

        # If all tables are booked for the given time slot
        if not form.instance.table_number:
            messages.warning(
                self.request, "Sorry, all tables are booked for this time."
            )
            return self.form_invalid(form)

        # Set the time of the booking
        form.instance.time_ordered = datetime.now()

        messages.success(self.request, "Booking successfully Made.")

        return super().form_valid(form)


class Reservations(ListView):
    # Shows a list of bookings the user has created
    model = Booking
    template_name = "mybookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by(
                                                                       "day",
                                                                       "time")


class BookingDelete(DeleteView):
    # Deletes a booking
    model = Booking
    success_url = reverse_lazy("bookings")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Booking deleted successfully.")
        return super().delete(request, *args, **kwargs)


class BookingUpdate(UpdateView):
    # a user can update an existing booking
    model = Booking
    fields = ["day", "time"]
    template_name = "reservations.html"
    success_url = reverse_lazy("bookings")

    # Changes the day field so the custom date picker gets initialised
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["day"].widget.attrs.update(
            {"id": "datepicker", "class": "text-center"}
        )
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["booking_id"] = self.kwargs["pk"]
        return context

    def form_valid(self, form):
        # Check if booking already exists for user and time
        if Booking.objects.filter(user=self.request.user, day=form.cleaned_data['day'], time=form.cleaned_data['time']).exists():
            messages.warning(self.request, 'You have already booked a table at this time.')
            return self.form_invalid(form)

        # Takes data In
        available_tables = TABLES_AVAILABLE
        booked_tables = Booking.objects.filter(
            day=form.cleaned_data["day"], time=form.cleaned_data["time"]
        ).values_list("table_number", flat=True)

        # Checks if the restaurant is fully booked. If not assigns table.
        if (len(available_tables) == len(booked_tables)):
            messages.warning(self.request, "Sorry, all tables are booked for this time.")
            return self.form_invalid(form)
        else:
            for table in available_tables:
                if table[0] not in booked_tables:
                    form.instance.table_number = table[0]
                    break
            form.instance.time_ordered = datetime.now()
            messages.success(self.request, "Booking successfully Updated.")
            return super().form_valid(form)
