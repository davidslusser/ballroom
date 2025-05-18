import random
from typing import Dict, Set
from .models import CalculationRequest


AVERAGE_DANCE_MINUTES = 5
SIMULATION_RUNS = 1000


def simulate_event(req: CalculationRequest) -> float:
    """Monte-Carlo simulation of an entire ballroom event.
    Repeats the event SIMULATION_RUNS times and returns the mean unique-partner
    count across *all* participants (leaders + followers).
    """
    leaders = list(req.leader_knowledge.keys())
    followers = list(req.follower_knowledge.keys())
    rounds = req.dance_duration_minutes // AVERAGE_DANCE_MINUTES

    cumulative_mean = 0.0

    for _ in range(SIMULATION_RUNS):
        danced_with: Dict[str, Set[str]] = {pid: set() for pid in leaders + followers}

        for _ in range(rounds):
            available_leaders = leaders.copy()
            available_followers = followers.copy()
            random.shuffle(available_leaders)
            random.shuffle(available_followers)

            for leader in list(available_leaders):
                if leader not in available_leaders:
                    continue
                for follower in list(available_followers):
                    common_styles = set(req.leader_knowledge[leader]).intersection(
                        req.follower_knowledge[follower]
                    )
                    if not common_styles:
                        continue

                    random.choice(tuple(common_styles))  # Simulate style choice
                    available_leaders.remove(leader)
                    available_followers.remove(follower)
                    danced_with[leader].add(follower)
                    danced_with[follower].add(leader)
                    break

        cumulative_mean += sum(len(partners) for partners in danced_with.values()) / len(danced_with)

    return round(cumulative_mean / SIMULATION_RUNS, 2)
