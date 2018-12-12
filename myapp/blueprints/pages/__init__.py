from sanic import Blueprint
from .hello import hello


pages = Blueprint.group(hello, url_prefix='')
