import pytest
import flask
from Server.blueprints.webpage_blueprint import webpage_blueprint


@pytest.fixture()
def app():
    app = flask.Flask(__name__)
    app.register_blueprint(webpage_blueprint)
    app.config.update({"TESTING": True})

    yield app

@pytest.fixture()
def client(app):
    return(app.test_client())
