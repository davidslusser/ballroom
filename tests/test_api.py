from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_calculate_partners_success():
    """Test the /calculate-partners endpoint with valid data."""
    payload = {
        "dance_duration_minutes": 30,
        "dance_styles": ["Waltz", "Tango"],
        "follower_knowledge": {
            "A": ["Waltz"],
            "B": ["Tango"]
        },
        "leader_knowledge": {
            "1": ["Waltz", "Tango"],
            "2": ["Tango"]
        },
        "total_followers": 2,
        "total_leaders": 2,
    }

    response = client.post("/calculate-partners", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert "average_dance_partners" in data
    assert isinstance(data["average_dance_partners"], float)


def test_invalid_leader_count():
    """Test the /calculate-partners endpoint with invalid leader count."""
    payload = {
        "dance_duration_minutes": 15,
        "dance_styles": ["Waltz"],
        "follower_knowledge": {
            "A": ["Waltz"]
        },
        "leader_knowledge": {
            "1": ["Waltz"],
            "2": ["Waltz"]  # only 2 leaders provided
        },
        "total_followers": 1,
        "total_leaders": 3,
    }

    response = client.post("/calculate-partners", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "total_leaders does not match leader_knowledge size"


def test_happy_path_small():
    """Minimal viable payload → 200 + float result."""
    payload = {
            "dance_duration_minutes": 10,
            "dance_styles": ["Waltz"],
            "follower_knowledge": {"A": ["Waltz"]},
            "leader_knowledge": {"1": ["Waltz"]},
            "total_followers": 1,
            "total_leaders": 1,
        }
    response = client.post("/calculate-partners", json=payload)
    assert response.status_code == 200
    assert isinstance(response.json()["average_dance_partners"], float)
    assert response.json()["average_dance_partners"] == 1.0


def test_no_common_dances():
    """No overlap → average must be 0.0."""
    payload ={
            "dance_duration_minutes": 30,
            "dance_styles": ["Waltz", "Tango"],
            "follower_knowledge": {"1": ["Tango"], "2": ["Tango"]},
            "leader_knowledge": {"A": ["Waltz"], "B": ["Waltz"]},
            "total_followers": 2,
            "total_leaders": 2,
        }
    response = client.post("/calculate-partners", json=payload)
    assert response.status_code == 200
    assert response.json()["average_dance_partners"] == 0.0


def test_large_imbalance_many_followers():
    """
    2 leaders vs 20 followers, lots of overlap.
    Average partners should be <= number of followers
    and > 0 since overlap exists.
    """
    payload = {
        "dance_duration_minutes": 60,
        "dance_styles": ["Waltz"],
        "follower_knowledge": {f"F{i}": ["Waltz"] for i in range(1, 21)},
        "leader_knowledge": {"A": ["Waltz"], "B": ["Waltz"]},
        "total_followers": 20,
        "total_leaders": 2,
    }
    response = client.post("/calculate-partners", json=payload)
    avg = response.json()["average_dance_partners"]
    assert response.status_code == 200
    assert 0.0 < avg <= 20.0
