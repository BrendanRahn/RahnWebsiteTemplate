import requests
import pytest
import sys 


def test_nav_connection(app):
    res = app.test_client().get("/")
    assert res.status == 200
    


def test_login_connection():
    res = requests.get("http://127.0.0.1:5000/login")

    assert res.status_code == 200
    assert "username" in res.text #put more accurate identifiers in headers of html


def test_home_connection():
    res = requests.get("http://127.0.0.1:5000/home")

    assert res.status_code == 200
    assert "Date of birth:"