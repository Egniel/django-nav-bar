from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag('template_tags/draw_menu.html', takes_context=True)
def draw_menu(context, slug):
    menu = Menu.objects.filter(slug=slug).first()
    if menu:
        return {'menu': menu, 'context': context}
    return {'menu': '', 'context': context}


@register.inclusion_tag('template_tags/dropdown.html', takes_context=True)
def dropdown(context, menu):
    return {'menu': menu, 'context': context}
