import pytest
from myapp import create_app
from sanic.websocket import WebSocketProtocol


@pytest.fixture(scope='session')
def app(request):
    app = create_app()
    return app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))
