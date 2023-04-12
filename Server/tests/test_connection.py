

def test_nav_connection(client):
    res = client.get("/")
    assert "navPage" in res.text
    assert res.status == "200 OK"


def test_login_connection(client):
    res = client.get("/login")
    assert "loginPage" in res.text
    assert res.status == "200 OK"


def test_home_connection(client):
    res = client.get("/home")
    assert "homePage" in res.text
    assert res.status == "200 OK"

    
