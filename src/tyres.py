# tyres.py
from weather import Weather

class Tyre:
    """
    Represents a tyre type with baseline performance and degradation properties.
    """

    # Recommended max laps in DRY conditions
    LAP_LIMITS_DRY = {
        "soft": 20,
        "medium": 30,
        "hard": 40,
        "intermediate": 15,  # if wrongly used in dry
        "wet": 15            # if wrongly used in dry
    }

    def __init__(self, name: str, base_lap_time: float, base_degradation_rate: float):
        """
        name: 'soft', 'medium', 'hard', 'intermediate', or 'wet'
        base_lap_time: Optimum lap time on this tyre (seconds)
        base_degradation_rate: baseline performance drop (seconds per lap)
        """
        self.name = name
        self.base_lap_time = base_lap_time
        self.base_degradation_rate = base_degradation_rate

    def lap_time(self, lap_number: int, weather: Weather, track_length_km: float, corner_count: int) -> float:
        """
        Calculate lap time for a specific lap considering progressive degradation and weather.
        """
        # Weather factor affects degradation
        weather_factor = weather.calculate_weather_factor()

        # Progressive degradation: small % increase per lap
        progressive_factor = 1 + 0.02 * (lap_number - 1)

        # Total degradation for this lap
        degradation_time = self.base_degradation_rate * weather_factor * progressive_factor

        # Weather mismatch penalty (wrong tyre/weather)
        penalty = weather.calculate_penalty(self.name, track_length_km, corner_count)

        return self.base_lap_time + degradation_time + penalty

    def stint_time(self, total_laps: int, weather: Weather, track_length_km: float, corner_count: int) -> float:
        """
        Calculate total time for a stint (sum of progressive lap times).
        """
        total_time = 0.0
        for lap in range(1, total_laps + 1):
            total_time += self.lap_time(lap, weather, track_length_km, corner_count)
        return total_time

    def check_lap_limit(self, requested_laps: int, weather: Weather) -> bool:
        """
        Warns if the requested laps exceed recommended limit.
        Returns True if risky.
        """
        # In wet races (light/heavy rain), NO enforced lap limits
        if weather.precipitation in ["light_rain", "heavy_rain"]:
            return False  # always safe in wet conditions

        # Dry race → apply limits
        base_limit = self.LAP_LIMITS_DRY.get(self.name, 20)

        if requested_laps > base_limit:
            print(f"⚠️ WARNING: Running {self.name.capitalize()} for {requested_laps} laps exceeds "
                  f"recommended {base_limit}-lap limit! High puncture risk.")
            return True
        return False


# Create tyre instances (baseline data - approximate)
soft = Tyre("soft", base_lap_time=90.0, base_degradation_rate=0.25)
medium = Tyre("medium", base_lap_time=92.0, base_degradation_rate=0.18)
hard = Tyre("hard", base_lap_time=94.0, base_degradation_rate=0.12)
intermediate = Tyre("intermediate", base_lap_time=96.0, base_degradation_rate=0.20)
wet = Tyre("wet", base_lap_time=100.0, base_degradation_rate=0.22)

tyres = {
    "soft": soft,
    "medium": medium,
    "hard": hard,
    "intermediate": intermediate,
    "wet": wet
}

# Quick test
if __name__ == "__main__":
    # Dry race check
    weather_dry = Weather("dry", "moderate")
    print("Lap 1 Soft:", soft.lap_time(1, weather_dry, 5.3, 16))
    print("Lap 10 Soft:", soft.lap_time(10, weather_dry, 5.3, 16))
    soft.check_lap_limit(25, weather_dry)  # should warn for soft

    # Wet race should skip limits
    weather_wet = Weather("light_rain", "cold")
    soft.check_lap_limit(50, weather_wet)  # should NOT warn
