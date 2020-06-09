from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render

from aerolinksma.shuttle.models import Reservation
from aerolinksma.shuttle.forms import ClientForm, ReservationForm


class CreateReservationView(generic.View):
    template_name = 'shuttle/index.html'
    client_form = ClientForm()
    reservation_form = ReservationForm()

    def get(self, request, *args, **kwars):
        context = {
            'client_form': self.client_form,
            'reservation_form': self.reservation_form,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        client_form = ClientForm(request.POST)
        reservation_form = ReservationForm(request.POST)

        if all((client_form.is_valid(), reservation_form.is_valid())):
            client = client_form.save()
            reservation = reservation_form.save(commit=False)
            reservation.client = client
            reservation.save()

            return HttpResponseRedirect(reverse('index'))