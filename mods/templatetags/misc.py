from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from mods.models import Category

register = template.Library()


@register.filter
@stringfilter
def get_category_icon(value):
    return mark_safe(Category.objects.get(label=value).icon)
