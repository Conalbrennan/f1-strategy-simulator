from tracks import tracks
from tyres import tyres
import math
import itertools

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

def find_optimal_strategy(track_name: str, weather: str):
    track = next((t for t in tracks if t.name == track_name), None)
    if not track:
        raise ValueError("Track not found.")

    if weather == "dry":
        compounds = ["soft", "medium", "hard"]
    elif weather == "wet":
        compounds = ["intermediate", "wet"]
    else:
        raise ValueError("Invalid weather type.")

    max_stints = 5
    best_strategy = None
    best_total_time = float('inf')
    pit_stop_penalty = track.pit_stop_loss

    def generate_strategies(remaining_laps, current_stints):
        if remaining_laps == 0:
            if len(current_stints) >= 2:  # ✅ at least 1 pit stop
                yield current_stints
            return
        if len(current_stints) >= max_stints:
            return
        for compound in compounds:
            tyre = tyres[compound]
            max_laps = min(tyre.lap_limit, remaining_laps)
            for laps in range(5, max_laps + 1):
                if laps < tyre.lap_limit // 2:
                    continue
                yield from generate_strategies(
                    remaining_laps - laps,
                    current_stints + [(compound, laps)]
                )

    seen = set()
    for stints in generate_strategies(track.laps, []):
        if any(i > 0 and stints[i][0] == stints[i - 1][0] for i in range(len(stints))):
            continue
        key = tuple(stints)
        if key in seen:
            continue
        seen.add(key)

        try:
            total_stint_time = 0
            stint_details = []
            for compound, laps in stints:
                lap_times = get_lap_times(track_name, compound, laps)
                stint_time = overall_stint_time(lap_times)
                total_stint_time += stint_time
                stint_details.append({
                    "compound": compound,
                    "laps": laps,
                    "time_str": format_total_time(stint_time)
                })

            pit_time = (len(stints) - 1) * pit_stop_penalty
            total_time = total_stint_time + pit_time

            if total_time < best_total_time:
                best_total_time = total_time
                best_strategy = stint_details
        except Exception:
            continue

    if best_strategy:
        return best_strategy, format_total_time(best_total_time), (len(best_strategy) - 1) * pit_stop_penalty
    else:
        raise ValueError("No valid strategy found.")
