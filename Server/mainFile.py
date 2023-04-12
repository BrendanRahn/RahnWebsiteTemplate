#not sure whether sub methods should be imported by name, or soley flask library
#TODO add status codes to routes
import flask
from Server.create_app import create_app




app = create_app()

with app.test_request_context():
    print (flask.url_for("static", filename="logoImage.jpeg"))