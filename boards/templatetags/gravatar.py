import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()

@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://www.gravatar.com/avatar/d1a99b21f516da58315a7380fc930c6c'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url