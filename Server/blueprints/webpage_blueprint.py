import flask
from flask import Blueprint

webpage_blueprint = Blueprint("ex_blueprint", __name__, template_folder="templates")



@webpage_blueprint.route("/")
def navPage():
    return flask.render_template("navPage.html")

@webpage_blueprint.route("/login", methods = ["GET", "POST"])
def loginPage():
    if (flask.request.method == "GET"):
        return flask.render_template("loginPage.html")
    
    if (flask.request.method == "POST"):
        #use module to verify login data

        return flask.redirect("/home")


@webpage_blueprint.route("/home")
def homePage():
    #TODO: figure out cookies to redirect to login page if not signed in
    return flask.render_template("homePage.html")
