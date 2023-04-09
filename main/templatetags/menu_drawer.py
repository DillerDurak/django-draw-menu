from django import template

from main.models import Menu

register = template.Library()

#Принимает строку, чтобы идентифицировать меню
@register.inclusion_tag('draw_menu.html')
def draw_menu(menu: str):
    '''Объявление в шаблоне - {% draw_menu 'название меню' %}'''
    #Делаем входящую строку строкой с большой буквы
    menu = menu.capitalize()
    m = Menu.objects.select_related('parent').filter(title=menu)[0]
    return {'menu': m}

