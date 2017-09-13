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


class BatteryCreateView(generic.CreateView):
    model = Battery
    form_class = BatteryCreateForm
    template_name = 'battery_create.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(kwargs)




class BatteryDeleteView(generic.DeleteView):
    model = Battery
    success_url = reverse_lazy('vehicle:vehicle')
    template_name = 'delete.html'


class MainView(generic.TemplateView):
    vehicle = None
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        self.vehicle = Vehicle.objects.get(pk=kwargs['pk'])
        vehicle_pk = kwargs['pk']
        vehicle_form = VehicleUpdateForm()
        battery_form = BatteryCreateForm()
        context = self.get_context_data(**kwargs)
        context['batteries'] = Battery.objects.filter(vehicle=self.vehicle)
        context['battery_form'] = battery_form
        context['vehicle_form'] = vehicle_form
        context['vehicle_pk'] = vehicle_pk
        context['name'] = Vehicle.objects.get(pk=vehicle_pk)
        return self.render_to_response(context)

