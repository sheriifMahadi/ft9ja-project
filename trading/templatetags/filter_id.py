from django import template
register = template.Library()

@register.filter(name='mongoId')
def mongoId(obj, attribute):
    obj = dict(obj)
    return obj.get(attribute)