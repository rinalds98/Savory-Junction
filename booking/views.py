from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Booking


class IndexView(TemplateView):
    template_name = 'index.html'


class MenuView(TemplateView):
    template_name = 'menu.html'


class BookingList(CreateView):
    model = Booking
    fields = ['day', 'time']
    template_name = 'reservations.html'

