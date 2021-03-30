from django import template

register = template.Library()


def val(value, arg):
    attrs = value.field.widget.attrs
    attrs['value'] = arg

    rendered = str(value)

    return rendered


register.filter('val', val)
