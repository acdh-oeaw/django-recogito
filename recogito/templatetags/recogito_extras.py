from django import template
register = template.Library()


@register.inclusion_tag('recogito/load_js.html', takes_context=True)
def load_recogito_js(context):
    values = {}
    return values
