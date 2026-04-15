import pytest
from demo_ecommerce.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_alias_page_loads(client):
    response = client.get("/home")
    assert response.status_code == 200


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_signup_page_loads(client):
    response = client.get("/signup")
    assert response.status_code == 200


def test_cart_page_loads(client):
    response = client.get("/cart")
    assert response.status_code == 200


def test_checkout_page_loads(client):
    response = client.get("/checkout")
    assert response.status_code in [200, 302]


def test_contact_page_loads(client):
    response = client.get("/contact")
    assert response.status_code == 200


def test_product_page_valid_id(client):
    response = client.get("/product/1")
    assert response.status_code == 200
