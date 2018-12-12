from sanic import Blueprint
from .hello import hello
from .todo import todo


api = Blueprint.group(hello, todo, url_prefix='/api')
