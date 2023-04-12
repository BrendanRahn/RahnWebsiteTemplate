import pytest
import flask
from Server.create_app import create_app
from Server.blueprints.webpage_blueprint import webpage_blueprint


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True})

    yield app



@pytest.fixture()
def client(app):
    return(app.test_client())
