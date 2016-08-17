from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from models import PriceList, ClientsAddresses, Clients, Mats


admin.site.register(ClientsAddresses, LeafletGeoAdmin)
admin.site.register(PriceList)
admin.site.register(Clients)
admin.site.register(Mats)
# Register your models here.
