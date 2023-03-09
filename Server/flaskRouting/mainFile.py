import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

test = "I am slug glug"

@app.route("/<string:slug>/")
def show_slug(slug):
    return "Slug says: {} ".format(slug)

@app.route("/html/")
def show_test():
    
    return flask.render_template("dummy_site.html")


