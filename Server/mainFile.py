#not sure whether sub methods should be imported by name, or soley flask library
#TODO add status codes to routes
import flask


app = flask.Flask(__name__)

@app.route("/")
def navPage():
    return flask.render_template("navPage.html")

@app.route("/login", methods = ["GET", "POST"])
def loginPage():
    if (flask.request.method == "GET"):
        return flask.render_template("loginPage.html")
    
    if (flask.request.method == "POST"):
        #use module to verify login data

        return flask.redirect("/home")


@app.route("/home")
def homePage():
    #TODO: figure out cookies to redirect to login page if not signed in
    return flask.render_template("homePage.html")
