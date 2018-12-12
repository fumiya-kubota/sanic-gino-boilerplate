from sanic import Blueprint
from .v1 import bp as v1_bp


api = Blueprint.group(v1_bp, url_prefix='/api')
