import pytest

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Days" in response.data

def test_post_show(client):
    response = client.post("/show", data={"days": "2"})
    assert response.status_code == 200
    assert b"Cases" in response.data

def test_post_show_integer_only(client):
    response = client.post("/show", data={"days": "xx"})
    assert response.status_code == 302
