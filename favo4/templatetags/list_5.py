from django import template
from ..models import Chara
register = template.Library()


@register.filter
def child_5(queryset, pk):
    return queryset.filter(content=pk).order_by('?')[0:7]
