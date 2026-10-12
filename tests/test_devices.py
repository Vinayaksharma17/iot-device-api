
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.device_service import DEVICES

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_devices():
    """Restore the in-memory data before and after each test."""
    original_devices = DEVICES.copy()

    yield

    DEVICES.clear()
    DEVICES.update(original_devices)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_devices():
    response = client.get("/devices")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_existing_device():
    response = client.get("/devices/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Temperature Sensor 01"


def test_missing_device_returns_404():
    response = client.get("/devices/999")

    assert response.status_code == 404


def test_create_device():
    response = client.post(
        "/devices",
        json={
            "name": "Pressure Sensor",
            "status": "online",
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == 3
    assert response.json()["name"] == "Pressure Sensor"


def test_invalid_status_is_rejected():
    response = client.post(
        "/devices",
        json={
            "name": "Pressure Sensor",
            "status": "maintenance",
        },
    )

    assert response.status_code == 422
    assert len(DEVICES) == 2


def test_short_name_is_rejected():
    response = client.post(
        "/devices",
        json={
            "name": "X",
            "status": "online",
        },
    )

    assert response.status_code == 422
    assert len(DEVICES) == 2


def test_invalid_device_id_returns_422():
    response = client.get("/devices/abc")

    assert response.status_code == 422
