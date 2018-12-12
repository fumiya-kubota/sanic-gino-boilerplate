from sanic import Sanic
from .config import get_configuration
from .blueprints import bp


def create_app():
    app = Sanic(__name__)
    config = get_configuration()
    app.config.from_object(config)
    app.blueprint(bp)
    return app