from sanic import Blueprint
from .hello import hello
from .todo import todo


bp = Blueprint.group(hello, todo, url_prefix='/v1')
