import pytest
from myapp import create_app
from myapp.config import TestingConfig
from myapp.models import db
from sanic.websocket import WebSocketProtocol
from sqlalchemy import create_engine


@pytest.fixture(scope='session')
def app(request):
    app = create_app()
    return app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))


@pytest.fixture()
def cleanup_db():
    testing_config = TestingConfig()
    db_host = testing_config.DB_HOST
    db_name = testing_config.DB_NAME
    engine = create_engine(f'postgresql://{db_host}')
    conn = engine.connect()
    try:
        conn.execution_options(isolation_level="AUTOCOMMIT").execute(f"CREATE DATABASE {db_name}")
    except Exception:
        pass
    rv = create_engine(f'postgresql://{db_host}/{db_name}')

    db.create_all(rv)
    yield rv

    db.drop_all(rv)
    rv.dispose()
