from django import template

register = template.Library()

@register.filter(name='mark_cut')
def mark_cut(value, arg):
    return value.split(arg)[0]
