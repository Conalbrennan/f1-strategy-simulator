class RaceTrack:
    def __init__(self, name, country, laps, lap_length_km, corners_left, corners_right,
                 direction, pit_stop_loss, tyre_wear,
                 soft_lap_time, medium_lap_time, hard_lap_time, intermediate_lap_time, wet_lap_time):
        self.name = name
        self.country = country
        self.laps = laps
        self.lap_length_km = lap_length_km
        self.corners_left = corners_left
        self.corners_right = corners_right
        self.direction = direction  # "clockwise" or "counterclockwise"
        self.pit_stop_loss = pit_stop_loss
        self.tyre_wear = tyre_wear  # 1-5 scale
        self.soft_lap_time = soft_lap_time
        self.medium_lap_time = medium_lap_time
        self.hard_lap_time = hard_lap_time
        self.intermediate_lap_time = intermediate_lap_time
        self.wet_lap_time = wet_lap_time

    def total_race_distance(self):
        return self.laps * self.lap_length_km

    def __repr__(self):
        return f"<RaceTrack {self.name} ({self.country}) - {self.laps} laps>"


tracks = []

# 1. Bahrain
tracks.append(RaceTrack(
    "Bahrain International Circuit", "Bahrain", 57, 5.412, 6, 9, "clockwise", 22, 4,
    90.0, 92.0, 94.0, 96.0, 100.0
))

# 2. Saudi Arabia (Jeddah)
tracks.append(RaceTrack(
    "Jeddah Corniche Circuit", "Saudi Arabia", 50, 6.174, 11, 16, "counterclockwise", 23, 3,
    89.5, 91.5, 93.5, 95.5, 99.5
))

# 3. Australia (Albert Park)
tracks.append(RaceTrack(
    "Albert Park Circuit", "Australia", 58, 5.278, 7, 9, "clockwise", 21, 2,
    88.2, 90.2, 92.2, 94.2, 98.2
))

# 4. Imola
tracks.append(RaceTrack(
    "Imola", "Italy", 63, 4.909, 7, 12, "clockwise", 22, 3,
    88.8, 90.8, 92.8, 94.8, 98.8
))

# 5. Monaco
tracks.append(RaceTrack(
    "Monaco", "Monaco", 78, 3.337, 11, 8, "clockwise", 19, 2,
    73.0, 75.0, 77.0, 79.0, 83.0
))

# 6. Spain (Barcelona-Catalunya)
tracks.append(RaceTrack(
    "Circuit de Barcelona-Catalunya", "Spain", 66, 4.675, 8, 10, "clockwise", 21, 3,
    87.0, 89.0, 91.0, 93.0, 97.0
))

# 7. Canada (Montreal)
tracks.append(RaceTrack(
    "Circuit Gilles Villeneuve", "Canada", 70, 4.361, 7, 8, "clockwise", 21, 3,
    85.6, 87.6, 89.6, 91.6, 95.6
))

# 8. Austria (Red Bull Ring)
tracks.append(RaceTrack(
    "Red Bull Ring", "Austria", 71, 4.318, 3, 7, "clockwise", 20, 3,
    75.3, 77.3, 79.3, 81.3, 85.3
))

# 9. Britain (Silverstone)
tracks.append(RaceTrack(
    "Silverstone Circuit", "United Kingdom", 52, 5.891, 10, 8, "clockwise", 21, 3,
    89.2, 91.2, 93.2, 95.2, 99.2
))

# 10. Hungary
tracks.append(RaceTrack(
    "Hungaroring", "Hungary", 70, 4.381, 8, 6, "clockwise", 22, 4,
    81.7, 83.7, 85.7, 87.7, 91.7
))

# 11. Belgium (Spa)
tracks.append(RaceTrack(
    "Circuit de Spa-Francorchamps", "Belgium", 44, 7.004, 9, 10, "clockwise", 22, 3,
    104.5, 106.5, 108.5, 110.5, 114.5
))

# 12. Netherlands (Zandvoort)
tracks.append(RaceTrack(
    "Circuit Zandvoort", "Netherlands", 72, 4.259, 7, 7, "clockwise", 21, 3,
    77.8, 79.8, 81.8, 83.8, 87.8
))

# 13. Italy (Monza)
tracks.append(RaceTrack(
    "Monza", "Italy", 53, 5.793, 4, 7, "clockwise", 20, 2,
    81.5, 83.5, 85.5, 87.5, 91.5
))

# 14. Singapore
tracks.append(RaceTrack(
    "Marina Bay Street Circuit", "Singapore", 61, 4.928, 11, 12, "counterclockwise", 25, 4,
    96.0, 98.0, 100.0, 102.0, 106.0
))

# 15. Japan (Suzuka)
tracks.append(RaceTrack(
    "Suzuka International Racing Course", "Japan", 53, 5.807, 8, 10, "clockwise", 21, 4,
    92.3, 94.3, 96.3, 98.3, 102.3
))

# 16. USA (COTA)
tracks.append(RaceTrack(
    "Circuit of the Americas", "USA", 56, 5.513, 9, 11, "counterclockwise", 22, 3,
    90.5, 92.5, 94.5, 96.5, 100.5
))

# 17. Mexico
tracks.append(RaceTrack(
    "Autódromo Hermanos Rodríguez", "Mexico", 71, 4.304, 6, 10, "clockwise", 22, 2,
    80.6, 82.6, 84.6, 86.6, 90.6
))

# 18. Brazil
tracks.append(RaceTrack(
    "Interlagos", "Brazil", 71, 4.309, 8, 6, "counterclockwise", 22, 3,
    81.0, 83.0, 85.0, 87.0, 91.0
))

# 19. Las Vegas
tracks.append(RaceTrack(
    "Las Vegas Street Circuit", "USA", 50, 6.201, 8, 9, "counterclockwise", 23, 2,
    90.0, 92.0, 94.0, 96.0, 100.0
))

# 20. Qatar (Lusail)
tracks.append(RaceTrack(
    "Lusail International Circuit", "Qatar", 57, 5.419, 6, 10, "clockwise", 22, 4,
    91.5, 93.5, 95.5, 97.5, 101.5
))

# 21. Abu Dhabi
tracks.append(RaceTrack(
    "Yas Marina Circuit", "UAE", 58, 5.281, 6, 10, "clockwise", 22, 3,
    90.1, 92.1, 94.1, 96.1, 100.1
))


# Debug: Print all tracks
if __name__ == "__main__":
    for track in tracks:
        print(track)
