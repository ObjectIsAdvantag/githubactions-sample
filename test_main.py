from  fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "foobar", "description": "The Foo Barters", "price": 10, "tax": 5},
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "foobar",
        "description": "The Foo Barters",
        "price": 10.0,
        "tax": 5.0, 
        "price_with_tax" : 15.0
    }

