from django.conf.urls import url

from .views import VehicleView, VehicleCreateView, BatteryUpdateView, VehicleUpdateView, BatteryDeleteView, BatteryCreateView

app_name = 'vehicle'
urlpatterns = [
    url(r'^vehicle/$', VehicleView.as_view(), name='vehicle'),
    url(r'^vehicle/add/$', VehicleCreateView.as_view(), name='vehicle_add'),
    url(r'^battery/update/(?P<pk>[0-9]+)/$', BatteryUpdateView.as_view(), name='battery'),
    # url(r'^vehicle/(?P<pk>[0-9]+)/$', MainView.as_view(), name='main'),
    url(r'^vehicle/update/(?P<pk>[0-9]+)/$', VehicleUpdateView.as_view(), name='vehicle_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', BatteryDeleteView.as_view(), name='delete'),
    url(r'^battery/add/$', BatteryCreateView.as_view(), name='battery_add'),

]