
def test_nav_connection(client):
    res = client.get("/")
    assert "BLUEPRINT" in res.text
    assert res.status == "200 OK"

    
