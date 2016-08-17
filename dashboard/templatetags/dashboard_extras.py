__author__ = 'udaw'

import datetime
from django import template

register = template.Library()

@register.simple_tag
def project_name():
    return 'Chistahoda dashboard'

@register.simple_tag
def clients_list():
    return 'Clients List'

@register.simple_tag
def details():
    return 'Details'

@register.simple_tag
def addresses_list():
    return 'Addreses List'

@register.simple_tag
def mats_list():
    return 'Mats List'

@register.simple_tag
def get_verbose_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name.title()

# @register.filter(name="get_field_verbose_name")
# def get_field_verbose_name(instance, arg):
#     # return instance._meta.get_field(arg).verbose_name
#     return instance._meta.get_field(arg).verbose_name.title()
# # register.filter('field_verbose_name', get_field_verbose_name)
#
#
# def get_queryset_field_verbose_name(queryset, arg):
#     return queryset.model._meta.get_field(arg).verbose_name
# register.filter('queryset_field_verbose_name', get_queryset_field_verbose_name)