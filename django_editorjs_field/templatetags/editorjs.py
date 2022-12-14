from django import template

from ..utils import render


register = template.Library()

register.simple_tag(render)
