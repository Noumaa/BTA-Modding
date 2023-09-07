from datetime import datetime

from django import template

register = template.Library()


@register.filter
def days_until(date):
    delta = datetime.date(date) - datetime.now().date()
    return str(delta.days)[1:] if str(delta.days)[1:] is not '' else '0'
