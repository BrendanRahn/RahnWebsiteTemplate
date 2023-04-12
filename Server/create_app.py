import flask
from Server.blueprints.webpage_blueprint import webpage_blueprint

def create_app():
    app = flask.Flask(__name__, static_url_path="/static")
    app.register_blueprint(webpage_blueprint)

    return app