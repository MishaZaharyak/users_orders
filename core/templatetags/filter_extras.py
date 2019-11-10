from django import template

register = template.Library()


@register.simple_tag
def get_url_with_params(_list, name, value):
    url = '?'
    i = 0
    for li in _list:
        i += 1
        new_value = value if li == name else _list[li]
        url += li + '=' + str(new_value) if len(_list) == i else li + '=' + str(new_value) + '&'
    if name not in _list:
        url += '&' + name + '=' + str(value) if len(_list) > 0 else name + '=' + str(value)
    return url
