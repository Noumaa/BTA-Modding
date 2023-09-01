from django import template

register = template.Library()


@register.simple_tag()
def debug_object_dump(var):
    return vars(var)
