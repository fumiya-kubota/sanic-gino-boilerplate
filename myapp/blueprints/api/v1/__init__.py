from sanic import Blueprint
from .hello import hello


bp = Blueprint.group(hello, url_prefix='/v1')
