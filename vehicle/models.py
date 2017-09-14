import random
import uuid
from django.urls import reverse

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Vehicle(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name = "Pojazd", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vehicle:vehicle')

    def batteries_on(self):
        on = self.batteries.filter(on=True).count()
        return on

    def batteries_all(self):
        all_batteries= self.batteries.all().count()
        return all_batteries

class Battery(models.Model):
    vehicle = models.ForeignKey('Vehicle', verbose_name = "Pojazd", related_name='batteries')
    ID = models.IntegerField(primary_key=True, unique=True)
    number = models.IntegerField(verbose_name='Numer baterii')
    on = models.BooleanField(default=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return str(self.ID)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.ID:
            self.ID = int('5' + ''.join(str(random.choice(list(range(1, 10000, 2))))))
            while Battery.objects.filter(ID=self.ID).exists():
                self.ID = int('5' + ''.join(str(random.choice(list(range(1, 10000, 2))))))

    def get_absolute_url(self):
        return reverse('vehicle:vehicle')

    def on_off(self):
        if self.on == True:
            return "ON"
        else:
            return "OFF"
