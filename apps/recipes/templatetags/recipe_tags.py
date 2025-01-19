from django import template

register = template.Library()


@register.filter
def short_description(desc):
  return desc[:50] + "..."