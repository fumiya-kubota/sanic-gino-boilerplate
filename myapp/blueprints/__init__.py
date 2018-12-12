from sanic import Blueprint
from .api import api
from .pages import pages


bp = Blueprint.group(api, pages)
