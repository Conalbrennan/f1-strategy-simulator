from tracks import tracks
from tyres import tyres
import math

def calculate_deg_rate(tyre_name: str, lap_number: int) -> float:
    tyre = tyres[tyre_name]
    lap_limit = tyre.lap_limit
    halfway = lap_limit // 2

    if lap_number <= halfway:
        return 0.0

    n = lap_number - halfway
    return tyre.base_degradation_rate * math.log1p(n)

def get_lap_times(track_name: str, tyre_name: str, stint_laps: int) -> list[float]:
    track = next((t for t in tracks if t.name == track_name), None)
    if not track:
        raise ValueError(f"Track '{track_name}' not found.")

    tyre = tyres[tyre_name]
    attr_name = f"{tyre_name}_lap_time"
    base_lap_time = getattr(track, attr_name)

    lap_times = []
    for lap in range(1, stint_laps + 1):
        deg = calculate_deg_rate(tyre_name, lap)
        lap_time = base_lap_time + deg
        lap_times.append(lap_time)

    return lap_times

def overall_stint_time(lap_times: list[float]) -> float:
    return sum(lap_times)

def format_total_time(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = seconds % 60
    return f"{mins}m {secs:.2f}s"
