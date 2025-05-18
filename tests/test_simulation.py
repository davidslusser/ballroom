from app.simulation import simulate_event
from app.models import CalculationRequest


def test_basic_paring():
    """Ensure algorithm returns 1 when all styles match."""
    req = CalculationRequest(
        total_leaders=1,
        total_followers=1,
        dance_styles=["Waltz"],
        leader_knowledge={"1": ["Waltz"]},
        follower_knowledge={"A": ["Waltz"]},
        dance_duration_minutes=10
    )

    result = simulate_event(req)
    assert isinstance(result, float)
    assert result == 1.0


def test_no_common_styles():
    """Ensure algorithm returns 0 when no common styles."""
    req = CalculationRequest(
        total_leaders=1,
        total_followers=1,
        dance_styles=["Waltz", "Tango"],
        leader_knowledge={"1": ["Waltz"]},
        follower_knowledge={"A": ["Tango"]},
        dance_duration_minutes=10
    )

    result = simulate_event(req)
    assert isinstance(result, float)
    assert result == 0.0


def test_large_imbalance():
    """Ensure algorithm scales & returns reasonable value."""
    req = CalculationRequest(
        dance_duration_minutes=120,
        dance_styles=["Waltz"],
        follower_knowledge={f"F{i}": ["Waltz"] for i in range(50)},
        leader_knowledge={f"L{i}": ["Waltz"] for i in range(5)},
        total_followers=50,
        total_leaders=5,
    )
    result = simulate_event(req)
    assert isinstance(result, float)
    assert 0.0 < result <= 50.0
