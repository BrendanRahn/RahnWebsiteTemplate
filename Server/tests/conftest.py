import pytest
import flask

from blueprint import ex_blueprint

@pytest.fixture()
def app():
    app = flask.Flask(__name__)
    app.register_blueprint(ex_blueprint)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


base_url = "http://localhost:5000"

@pytest.fixture()
def nav_url():
    return base_url

@pytest.fixture()
def login_url():
    return (base_url + "/login")

@pytest.fixture()
def home_url():
    return (base_url + "/home")

