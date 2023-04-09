#not sure whether sub methods should be imported by name, or soley flask library
#TODO add status codes to routes
import flask
from Server.blueprints.webpage_blueprint import webpage_blueprint



app = flask.Flask(__name__)
app.register_blueprint(webpage_blueprint)

