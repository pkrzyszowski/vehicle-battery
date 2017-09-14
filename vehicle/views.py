from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import VehicleCreateForm, VehicleUpdateForm, BatteryCreateForm, BatteryUpdateForm
from .models import Vehicle, Battery


class VehicleView(generic.ListView):
    queryset = Vehicle.objects.all()
    context_object_name = 'vehicles'
    template_name = 'vehicle.html'


class VehicleCreateView(generic.CreateView):
    model = Vehicle
    form_class = VehicleCreateForm
    template_name = 'vehicle_create.html'


class BatteryUpdateView(generic.UpdateView):
    model = Battery
    template_name = 'battery.html'
    form_class = BatteryUpdateForm


class VehicleUpdateView(generic.UpdateView):
    vehicle = None
    model = Vehicle
    form_class = VehicleUpdateForm
    template_name = 'vehicle_update.html'

    def get(self, request, *args, **kwargs):
        self.vehicle = Vehicle.objects.get(pk=kwargs['pk'])
        return super().get(request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batteries'] = Battery.objects.filter(vehicle=self.vehicle)
        return context

class BatteryCreateView(generic.CreateView):
    vehicle_pk=None
    model = Battery
    form_class = BatteryCreateForm
    template_name = 'battery_create.html'


class BatteryDeleteView(generic.DeleteView):
    model = Battery
    success_url = reverse_lazy('vehicle:vehicle')
    template_name = 'delete.html'
