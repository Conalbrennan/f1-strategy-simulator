from tracks import tracks
from tyres import tyres
import math

def calculate_deg_rate(tyre_name: str, lap_number: int) -> float:
    """
    Calculate degradation factor for a given tyre and lap number.
    Deg only applies after halfway point of tyre's lifespan.
    """
    tyre = tyres[tyre_name]
    lap_limit = tyre.lap_limit
    halfway = lap_limit // 2

    if lap_number <= halfway:
        return 0.0

    # Progressive degradation after halfway
    n = lap_number - halfway
    return tyre.base_degradation_rate * math.log1p(n)

def get_lap_times(track_name: str, tyre_name: str, stint_laps: int) -> list[float]:
    """
    Returns a list of lap times for a stint on a given track and tyre.
    """
    track = next((t for t in tracks if t.name == track_name), None)
    if not track:
        raise ValueError(f"Track '{track_name}' not found.")

    tyre = tyres[tyre_name]
    halfway = tyre.lap_limit // 2

    # Get base lap time from track
    attr_name = f"{tyre_name}_lap_time"
    base_lap_time = getattr(track, attr_name)

    lap_times = []

    for lap in range(1, stint_laps + 1):
        deg = calculate_deg_rate(tyre_name, lap)
        lap_time = base_lap_time + deg
        lap_times.append(lap_time)

    return lap_times

def overall_stint_time(lap_times: list[float]) -> float:
    """
    Sum total time of a list of lap times.
    """
    return sum(lap_times)

# === TESTING LOOP ===
if __name__ == "__main__":
    track_name = input("Enter track name (e.g. Austria): ").strip().title()
    track = next((t for t in tracks if t.name == track_name), None)

    if not track:
        print("Track not found.")
        exit()

    laps_remaining = track.laps
    print(f"\nTotal race laps: {track.laps}\n")

    while laps_remaining > 0:
        print(f"Laps remaining: {laps_remaining}")
        tyre = input("Enter tyre compound (soft, medium, hard, intermediate, wet): ").strip().lower()
        stint_laps = int(input("Enter number of laps for this stint: "))

        if stint_laps > laps_remaining:
            print("⚠️ Stint exceeds remaining laps. Try again.\n")
            continue

        lap_times = get_lap_times(track_name, tyre, stint_laps)
        stint_total = overall_stint_time(lap_times)
        mins = int(stint_total // 60)
        secs = stint_total % 60

        print(f"\nLap times for {tyre} stint ({stint_laps} laps):")
        print([round(t, 2) for t in lap_times])
        print(f"Total stint time: {mins}m {secs:.2f}s\n")

        laps_remaining -= stint_laps

    print("✅ Race distance reached.")
