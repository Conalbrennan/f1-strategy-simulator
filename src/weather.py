# weather.py

class Weather:
    """
    Represents weather conditions and their effect on tyre degradation and lap time.
    """

    # Factor multipliers for precipitation (rain)
    PRECIPITATION_FACTORS = {
        "dry": 1.0,
        "light_rain": 1.2,   # Slightly higher degradation and slower lap times
        "heavy_rain": 1.5    # Much higher degradation and lap time impact
    }

    # Factor multipliers for temperature
    TEMPERATURE_FACTORS = {
        "cold": 0.9,        # Less degradation but potentially less grip
        "moderate": 1.0,    # Baseline
        "hot": 1.3          # Higher degradation due to heat
    }

    def __init__(self, precipitation: str, temperature: str):
        """
        precipitation: 'dry', 'light_rain', or 'heavy_rain'
        temperature: 'cold', 'moderate', or 'hot'
        """
        if precipitation not in self.PRECIPITATION_FACTORS:
            raise ValueError(f"Invalid precipitation condition: {precipitation}")
        if temperature not in self.TEMPERATURE_FACTORS:
            raise ValueError(f"Invalid temperature condition: {temperature}")

        self.precipitation = precipitation
        self.temperature = temperature

    def calculate_weather_factor(self) -> float:
        """
        Combines precipitation and temperature to get an overall degradation multiplier.
        """
        precipitation_factor = self.PRECIPITATION_FACTORS[self.precipitation]
        temperature_factor = self.TEMPERATURE_FACTORS[self.temperature]

        # Combined factor multiplies both
        return precipitation_factor * temperature_factor

    def calculate_penalty(self, tyre_type: str, track_length_km: float, corner_count: int) -> float:
        """
        Calculates extra lap time penalty (in seconds) if tyres don't match weather.
        Penalty scales with track length and corner count.

        tyre_type: 'soft', 'medium', 'hard', 'intermediate', 'wet'
        """
        base_penalty = 0.0

        # Case 1: Slick tyres (soft/medium/hard) used in rain
        if tyre_type in ["soft", "medium", "hard"] and self.precipitation != "dry":
            base_penalty = 3.0  # baseline per km

        # Case 2: Wet/intermediate tyres used in dry
        elif tyre_type in ["intermediate", "wet"] and self.precipitation == "dry":
            base_penalty = 1.5  # overheating

        # Case 3: Intermediate tyre in heavy rain (undergrip)
        elif tyre_type == "intermediate" and self.precipitation == "heavy_rain":
            base_penalty = 2.5  # extra penalty beyond normal rain

        # Case 4: Wet tyre in light rain (too much tyre, overheats)
        elif tyre_type == "wet" and self.precipitation == "light_rain":
            base_penalty = 2.0  # overheats when track isn’t wet enough

        # Scale penalty by track characteristics
        # Longer tracks and more corners amplify penalty
        penalty = base_penalty * track_length_km * (1 + (corner_count / 20.0))
        return penalty

    def summary(self):
        """
        Returns a summary of the weather settings and factor.
        """
        return {
            "precipitation": self.precipitation,
            "temperature": self.temperature,
            "weather_factor": self.calculate_weather_factor()
        }


# Example usage
if __name__ == "__main__":
    # Example: Light rain and hot conditions
    weather = Weather("light_rain", "hot")
    factor = weather.calculate_weather_factor()
    penalty = weather.calculate_penalty("intermediate", track_length_km=5.8, corner_count=16)

    print(f"Weather Factor: {factor}")
    print(f"Lap Penalty (Intermediates): {penalty:.2f} seconds")
