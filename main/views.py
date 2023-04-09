from django.shortcuts import render, get_object_or_404

from .models import Menu

def home(request):
    '''Домашняя страница'''

    return render(request, 'home.html')

def menu(request):
    '''Рендер страницы со всеми главными меню'''

    menus = Menu.objects.select_related("parent").filter(parent=None)
    return render(request, 'menu.html', {'menus': menus})

def submenu(request, menu):
    '''Отображение конкретного подменю'''

    menu = menu.capitalize()
    m = Menu.objects.select_related("parent").filter(title=menu)[0]
    return render(request, 'submenu.html', {'menu': m})

