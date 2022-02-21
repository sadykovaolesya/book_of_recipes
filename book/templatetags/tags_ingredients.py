from django import template
register = template.Library()

from book.models import Ingredient

@register.simple_tag()
def get_ingredients():
    return Ingredient.objects.all()