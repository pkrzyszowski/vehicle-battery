from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
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
    vehicle=None
    model = Battery
    template_name = 'battery.html'
    form_class = BatteryUpdateForm

    def dispatch(self, request, *args, **kwargs):
        self.battery = get_object_or_404(Battery, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.vehicle = self.battery.vehicle
        self.object.ID = self.battery.ID
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('vehicle:vehicle_update', kwargs={'pk': self.object.vehicle.ID})


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
    vehicle = None
    model = Battery
    form_class = BatteryCreateForm
    template_name = 'battery_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle'] = self.vehicle
        return context

    def dispatch(self, request, *args, **kwargs):
        self.vehicle = get_object_or_404(Vehicle, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.vehicle = self.vehicle
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('vehicle:vehicle_update', kwargs={'pk': self.vehicle.ID})


class BatteryDeleteView(generic.DeleteView):
    model = Battery
    success_url = reverse_lazy('vehicle:vehicle')
    template_name = 'delete.html'
