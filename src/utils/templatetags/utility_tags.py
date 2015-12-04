#utils/templatetags/utility_tags.py
# -*- coding: UTF-8 -*-
import urllib
from django import template
from django.utils.encoding import force_str
register = template.Library()

### TAGS ###

@register.simple_tag(takes_context=True)
def append_to_query(context, **kwargs):
    """ Renders a link with modified current query parameters """
    query_params = context['request'].GET.copy()
    for key, value in kwargs.items():
        query_params[key] = value
    query_string = u""
    if len(query_params):
        query_string += u"?%s" % urllib.urlencode([
            (key, force_str(value)) for (key, value) in
            query_params. iteritems() if value 
        ]).replace('&', '&amp;')
    return query_string