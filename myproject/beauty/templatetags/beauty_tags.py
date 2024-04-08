from django import template

from beauty import views

register = template.Library()


@register.simple_tag(name='cat_tags')
def simple_tags():
    return views.category_db


@register.inclusion_tag('beauty/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.category_db
    return {'cats': cats, 'cat_selected': cat_selected}
