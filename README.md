# Django-приложение для отрисовки меню 
## Использование:
1. В панели админа создайте записи с меню/подменю
2. Загрузите template tag на нужную вам страницу ( {% load menu_drawer %} )
2. Далее, для отрисовки используйте template tag {% draw_menu 'Название меню' %}
 

```html
{% load menu_drawer %}

{% block content %}
    <div class="menu">
        {% draw_menu 'food' %}
    </div>
{% endblock %}
```
