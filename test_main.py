from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tesena test API is running!"}

def test_calculate_discount():
    response = client.post(
        "/discount",
        json={"original_price": 1000, "discount_percent": 20}
    )
    assert response.status_code == 200
    assert response.json() == {
        "original_price": 1000.0,
        "discount_percent": 20.0,
        "saved_amount": 200.0,
        "final_price": 800.0,
    }

def test_calculate_discount_with_invalid_percent():
    response = client.post(
        "/discount",
        json={"original_price": 1000, "discount_percent": 120}
    )
    assert response.status_code == 422

def test_password_check_strong_password():
    response = client.post(
        "/password-check",
        json={"password": "Heslo999!"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "is_strong": True,
        "checks": {
            "has_min_length": True,
            "has_uppercase": True,
            "has_lowercase": True,
            "has_digit": True,
            "has_special": True,
        },
    }

def test_password_check_weak_password():
    response = client.post(
        "/password-check",
        json={"password": "tesena"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "is_strong": False,
        "checks": {
            "has_min_length": False,
            "has_uppercase": False,
            "has_lowercase": True,
            "has_digit": False,
            "has_special": False,
        },
    }

def test_password_check_empty_password():
    response = client.post(
        "/password-check",
        json={"password": ""}
    )
    assert response.status_code == 422