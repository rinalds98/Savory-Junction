from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Booking, TABLES_AVAILABLE
from datetime import datetime


class IndexView(TemplateView):
    template_name = 'index.html'


class MenuView(TemplateView):
    template_name = 'menu.html'


class BookingList(CreateView):
    model = Booking
    fields = ['day', 'time']
    template_name = 'reservations.html'
    success_url = reverse_lazy('home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['day'].widget.attrs.update({'id': 'datepicker'})
        return form

    def form_valid(self, form):
        # Assign user to the booking
        form.instance.user = self.request.user

        # Check if booking already exists for user and time
        if Booking.objects.filter(user=form.instance.user, day=form.cleaned_data['day'], time=form.cleaned_data['time']).exists():
            messages.warning(self.request, 'You have already booked a table at this time.')
            return self.form_invalid(form)

        # Find available table for booking
        available_tables = TABLES_AVAILABLE
        booked_tables = Booking.objects.filter(day=form.cleaned_data['day'],
                                                time=form.cleaned_data['time']).values_list('table_number', flat=True)
        for table in available_tables:
            if table[0] not in booked_tables:
                form.instance.table_number = table[0]
                break

        # If all tables are booked for the given time slot
        if not form.instance.table_number:
            messages.warning(self.request, 'Sorry, all tables are booked for this time.')
            return self.form_invalid(form)

        # Set the time of the booking
        form.instance.time_ordered = datetime.now()

        return super().form_valid(form)
