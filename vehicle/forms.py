from django import forms
from django.forms import ModelForm, SelectMultiple
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.http import HttpResponseRedirect

from .models import Vehicle, Battery


class VehicleCreateForm(forms.ModelForm):
    number_of_battery = forms.IntegerField(label='Liczba baterii')
    class Meta:
        model = Vehicle
        fields = '__all__'

    def save(self, *args, **kwargs):
        vehicle = super().save()
        number = self.cleaned_data['number_of_battery']
        if number:
            for x in range(number):
                Battery.objects.create(vehicle=vehicle, number=x+1)
        return vehicle


class VehicleUpdateForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ['name']


class BatteryUpdateForm(forms.ModelForm):

    class Meta:
        model = Battery
        fields = '__all__'

class BatteryCreateForm(forms.ModelForm):

    class Meta:
        model = Battery
        fields = '__all__'
