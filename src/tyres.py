class Tyre:
    """
    Represents a tyre compound with degradation characteristics and lap limit.
    """

    def __init__(self, name: str, base_degradation_rate: float, lap_limit: int):
        """
        name: Tyre compound name ('soft', 'medium', 'hard', etc.)
        base_degradation_rate: Degradation per lap (in seconds)
        lap_limit: Recommended maximum laps before performance drops sharply
        """
        self.name = name
        self.base_degradation_rate = base_degradation_rate
        self.lap_limit = lap_limit


# Create tyre instances (baseline data - approximate)
soft = Tyre("soft", base_degradation_rate=0.25, lap_limit=20)
medium = Tyre("medium", base_degradation_rate=0.18, lap_limit=30)
hard = Tyre("hard", base_degradation_rate=0.12, lap_limit=40)
intermediate = Tyre("intermediate", base_degradation_rate=0.10, lap_limit=40)  # wet-only
wet = Tyre("wet", base_degradation_rate=0.08, lap_limit=40)                    # wet-only

# Tyre lookup dictionary
tyres = {
    "soft": soft,
    "medium": medium,
    "hard": hard,
    "intermediate": intermediate,
    "wet": wet
}
