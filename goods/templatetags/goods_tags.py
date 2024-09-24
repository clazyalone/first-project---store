from django.utils.http import urlencode
from django import template

from goods.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    print(query)
    query.update(kwargs)
    print(query)
    return urlencode(query)
