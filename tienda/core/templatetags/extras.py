from django import template

register = template.Library()

@register.filter
def pluck(list_of_dicts, key):
    return [d.get(key) for d in list_of_dicts]
