__author__ = 'udaw'

from django.conf.urls import url
from dashboard import views

urlpatterns = [
    # url(r'^mats/$', views.mats, name='mats'),
    url(r'^clients/$', views.ClientListView.as_view(), name='clients'),
    url(r'^addresses/$', views.AddressesListView.as_view(), name='addresses'),
    url(r'^mats/$', views.MatsListView.as_view(), name='mats'),

    url(r'^clients/(?P<pk>[0-9]+)/$', views.ClientDetailView.as_view(), name='client_detail'),
    url(r'^addresses/(?P<pk>[0-9]+)/$', views.AddressesDetailView.as_view(), name='address_detail'),
    url(r'^mats/(?P<pk>[0-9]+)/$', views.MatsDetailView.as_view(), name='mat_detail'),
]