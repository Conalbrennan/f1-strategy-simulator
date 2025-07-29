from tracks import tracks
from tyres import soft, medium, hard, intermediate, wet
from weather import Weather

# Map tyre names to objects
tyre_options = {
    "soft": soft,
    "medium": medium,
    "hard": hard,
    "intermediate": intermediate,
    "wet": wet
}

def format_time(total_seconds: float) -> str:
    """Convert total seconds into XX min YY.s format."""
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    return f"{minutes} min {seconds:.2f} sec"

def choose_track():
    print("\n=== F1 Strategy Simulator ===\n")
    print("Available Tracks:")
    for i, track in enumerate(tracks, start=1):
        print(f"{i}. {track.name} ({track.country}) - {track.lap_length_km} km, {track.laps} laps")

    choice = int(input("\nSelect a track number: ")) - 1
    return tracks[choice]

def display_track_info(track):
    print(f"\n--- {track.name} ({track.country}) ---")
    print(f"Laps: {track.laps}")
    print(f"Lap length: {track.lap_length_km} km")
    print(f"Corners: {track.corners_left + track.corners_right} "
          f"({track.corners_left} left / {track.corners_right} right)")
    print(f"Direction: {track.direction}")
    print(f"Pit stop loss: {track.pit_stop_loss} sec")
    print(f"Tyre wear factor: {track.tyre_wear}")
    print("Sectors:")
    for idx, sector in enumerate(track.sectors, start=1):
        print(f"  Sector {idx}: {sector['length']} km, corners {sector['corners']}")

def choose_weather():
    print("\nWeather options:")
    print("Precipitation: 1) Dry  2) Light Rain  3) Heavy Rain")
    element_choice = int(input("Choose precipitation (1-3): "))
    precipitation = ["dry", "light_rain", "heavy_rain"][element_choice - 1]

    print("\nTemperature: 1) Cold  2) Moderate  3) Hot")
    temp_choice = int(input("Choose temperature (1-3): "))
    temperature = ["cold", "moderate", "hot"][temp_choice - 1]

    return Weather(precipitation, temperature)

def build_strategy(track, weather):
    total_stints = []
    used_tyres = set()
    laps_remaining = track.laps
    total_time = 0.0

    is_wet_race = weather.precipitation in ["light_rain", "heavy_rain"]

    print("\n--- Build Your Strategy ---")
    if is_wet_race:
        print("Wet race detected → No requirement for 2 tyre types or lap limits.")
    else:
        print("Dry race → You must have at least 2 stints and 2 different tyre types.")

    while laps_remaining > 0:
        # Choose tyre
        tyre_choice = input(f"\nChoose tyre (soft/medium/hard/intermediate/wet): ").strip().lower()
        if tyre_choice not in tyre_options:
            print("Invalid tyre choice. Try again.")
            continue

        tyre = tyre_options[tyre_choice]
        used_tyres.add(tyre_choice)

        # Laps for this stint
        stint_laps = int(input(f"How many laps for this stint? Laps remaining: {laps_remaining}: "))

        if stint_laps > laps_remaining or stint_laps <= 0:
            print("Invalid lap count. Try again.")
            continue

        # ✅ NEW: Check lap safety limit → give restart option if risky
        if tyre.check_lap_limit(stint_laps, weather):
            restart_choice = input("Do you want to restart full strategy planning? (yes/no): ").strip().lower()
            if restart_choice.startswith("y"):
                print("\nRestarting full strategy planning...")
                return build_strategy(track, weather)

        # Calculate stint time
        stint_time = tyre.stint_time(
            total_laps=stint_laps,
            weather=weather,
            track_length_km=track.lap_length_km,
            corner_count=(track.corners_left + track.corners_right)
        )
        total_stints.append((tyre_choice, stint_laps, stint_time))
        total_time += stint_time

        # Subtract laps
        laps_remaining -= stint_laps

        # Add pit stop loss (except after final stint)
        if laps_remaining > 0:
            total_time += track.pit_stop_loss

        # If finished but invalid strategy (only one stint or one tyre in dry)
        if laps_remaining == 0 and not is_wet_race:
            if len(total_stints) < 2 or len(used_tyres) < 2:
                print("\nInvalid strategy: must have at least 2 stints and 2 tyre types in dry conditions.")
                return build_strategy(track, weather)

    # Print summary
    print("\n--- Strategy Summary ---")
    for idx, (tyre_type, laps, time) in enumerate(total_stints, start=1):
        print(f"Stint {idx}: {tyre_type.capitalize()} for {laps} laps → {format_time(time)}")

    print(f"\nTotal Race Time (including pit stops): {format_time(total_time)}")

if __name__ == "__main__":
    # 1. Choose track
    track = choose_track()
    display_track_info(track)

    # 2. Choose weather
    weather = choose_weather()

    # 3. Build strategy
    build_strategy(track, weather)
