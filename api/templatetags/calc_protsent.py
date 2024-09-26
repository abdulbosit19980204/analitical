from unicodedata import decimal

from django import template

register = template.Library()


@register.filter
def calc_protsent(value, arg) -> float:
    protsent = (100 * arg) / value
    return protsent
