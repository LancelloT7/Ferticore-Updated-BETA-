from django import template
from produtos.models import Produto

register = template.Library()

@register.filter
def product(product_id):
    """
    Recebe um product_id e retorna o objeto Produto correspondente.
    """
    try:
        return Produto.objects.get(id=product_id)
    except Produto.DoesNotExist:
        return None
    
@register.filter
def multiply(value, arg):
    """
    Multiplica o valor pelo argumento.
    """
    return value * arg