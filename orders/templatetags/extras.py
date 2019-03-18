from django import template
import datetime

register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '$')

register.filter('cut', cut)

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)