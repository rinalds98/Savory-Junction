from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Booking


class BookingList(CreateView):
    model = Booking
    fields = ['day', 'time']
    template_name = 'index.html'
