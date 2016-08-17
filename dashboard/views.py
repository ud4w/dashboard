from django.views.generic import ListView, DetailView
from models import Clients, ClientsAddresses, Mats


# from django.shortcuts import render
#
# def mats(request):
#     return render(request, "dashboard/mats.html", {"mats": Mats.objects.all()})

class ClientListView(ListView):
    model = Clients
    context_object_name = 'clients'
    template_name = 'dashboard/clients_view.html'


class AddressesListView(ListView):
    model = ClientsAddresses
    context_object_name = 'addresses'
    template_name = 'dashboard/addresses_view.html'


class MatsListView(ListView):
    model = Mats
    context_object_name = 'mats'
    template_name = 'dashboard/mats_view.html'


class ClientDetailView(DetailView):
    model = Clients
    template_name = 'dashboard/details_view.html'


class AddressesDetailView(DetailView):
    model = ClientsAddresses
    template_name = 'dashboard/details_view.html'


class MatsDetailView(DetailView):
    model = Mats
    template_name = 'dashboard/details_view.html'

    # def client_fields(self):
    #     return model._meta.fields

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['client_fields'] = Clients._meta.get_all_field_names().verbose_name.title()
    #     # context['client_fields'] = Clients._meta.get_fields().verbose_name.title()
    #     print context
    #     return context
