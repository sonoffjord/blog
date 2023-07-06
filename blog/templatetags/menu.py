from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(class_menu='sub-menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'class_menu': class_menu}