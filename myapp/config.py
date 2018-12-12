import os


class Config:
    # DATABASE_HOST = 'postgresql+asyncpg://sapl@127.0.0.1:5432'
    DB_HOST = 'myapp@127.0.0.1:5432'
    DB_NAME = 'myapp'


class TestingConfig:
    DB_HOST = 'myapp@127.0.0.1:5432'
    DB_NAME = 'myapp'


def get_configuration():
    if os.getenv('testing'):
        return TestingConfig()
    return Config()
