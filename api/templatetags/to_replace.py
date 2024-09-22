from django import template

register = template.Library()


@register.filter
def to_replace(value, key):
    return value.replace('@', key)
