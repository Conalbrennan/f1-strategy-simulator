class RaceTrack:
    def __init__(self, name, country, laps, lap_length_km, corners_left, corners_right,
                 direction, pit_stop_loss, tyre_wear, sectors):
        self.name = name
        self.country = country
        self.laps = laps
        self.lap_length_km = lap_length_km
        self.corners_left = corners_left
        self.corners_right = corners_right
        self.direction = direction  # "clockwise" or "counterclockwise"
        self.pit_stop_loss = pit_stop_loss
        self.tyre_wear = tyre_wear  # 1-5 scale
        self.sectors = sectors  # list of dicts: {"length": float, "corners": list[int]}

    def total_race_distance(self):
        return self.laps * self.lap_length_km

    def __repr__(self):
        return f"<RaceTrack {self.name} ({self.country}) - {self.laps} laps>"


tracks = []

# 1. Bahrain
tracks.append(RaceTrack(
    name="Bahrain International Circuit",
    country="Bahrain",
    laps=57,
    lap_length_km=5.412,
    corners_left=6,
    corners_right=9,
    direction="clockwise",
    pit_stop_loss=22,
    tyre_wear=4,
    sectors=[
        {"length": 2.2, "corners": [1, 2, 3, 4]},
        {"length": 1.8, "corners": [5, 6, 7, 8, 9]},
        {"length": 1.4, "corners": [10, 11, 12, 13, 14, 15]}
    ]
))

# 2. Saudi Arabia (Jeddah)
tracks.append(RaceTrack(
    name="Jeddah Corniche Circuit",
    country="Saudi Arabia",
    laps=50,
    lap_length_km=6.174,
    corners_left=11,
    corners_right=16,
    direction="counterclockwise",
    pit_stop_loss=23,
    tyre_wear=3,
    sectors=[
        {"length": 2.3, "corners": [1, 2, 3, 4]},
        {"length": 2.0, "corners": [5, 6, 7, 8, 9, 10, 11]},
        {"length": 1.9, "corners": [12, 13, 14, 15, 16, 17]}
    ]
))

# 3. Australia (Albert Park)
tracks.append(RaceTrack(
    name="Albert Park Circuit",
    country="Australia",
    laps=58,
    lap_length_km=5.278,
    corners_left=7,
    corners_right=9,
    direction="clockwise",
    pit_stop_loss=21,
    tyre_wear=2,
    sectors=[
        {"length": 1.9, "corners": [1, 2, 3, 4]},
        {"length": 1.7, "corners": [5, 6, 7, 8, 9]},
        {"length": 1.6, "corners": [10, 11, 12, 13, 14]}
    ]
))

# 4. Imola
tracks.append(RaceTrack(
    name="Imola",
    country="Italy",
    laps=63,
    lap_length_km=4.909,
    corners_left=7,
    corners_right=12,
    direction="clockwise",
    pit_stop_loss=22,
    tyre_wear=3,
    sectors=[
        {"length": 1.7, "corners": [1, 2, 3]},
        {"length": 1.6, "corners": [4, 5, 6, 7, 8, 9]},
        {"length": 1.6, "corners": [10, 11, 12, 13, 14, 15]}
    ]
))

# 5. Monaco
tracks.append(RaceTrack(
    name="Monaco",
    country="Monaco",
    laps=78,
    lap_length_km=3.337,
    corners_left=11,
    corners_right=8,
    direction="clockwise",
    pit_stop_loss=19,
    tyre_wear=2,
    sectors=[
        {"length": 1.1, "corners": [1, 2, 3]},
        {"length": 1.2, "corners": [4, 5, 6, 7, 8]},
        {"length": 1.0, "corners": [9, 10, 11, 12, 13, 14]}
    ]
))

# 6. Spain (Barcelona-Catalunya)
tracks.append(RaceTrack(
    name="Circuit de Barcelona-Catalunya",
    country="Spain",
    laps=66,
    lap_length_km=4.675,
    corners_left=8,
    corners_right=10,
    direction="clockwise",
    pit_stop_loss=21,
    tyre_wear=3,
    sectors=[
        {"length": 1.6, "corners": [1, 2, 3]},
        {"length": 1.5, "corners": [4, 5, 6, 7, 8]},
        {"length": 1.6, "corners": [9, 10, 11, 12, 13, 14]}
    ]
))

# 7. Canada (Montreal)
tracks.append(RaceTrack(
    name="Circuit Gilles Villeneuve",
    country="Canada",
    laps=70,
    lap_length_km=4.361,
    corners_left=7,
    corners_right=8,
    direction="clockwise",
    pit_stop_loss=21,
    tyre_wear=3,
    sectors=[
        {"length": 1.5, "corners": [1, 2, 3]},
        {"length": 1.4, "corners": [4, 5, 6, 7, 8]},
        {"length": 1.5, "corners": [9, 10, 11, 12, 13, 14]}
    ]
))

# 8. Austria (Red Bull Ring)
tracks.append(RaceTrack(
    name="Red Bull Ring",
    country="Austria",
    laps=71,
    lap_length_km=4.318,
    corners_left=3,
    corners_right=7,
    direction="clockwise",
    pit_stop_loss=20,
    tyre_wear=3,
    sectors=[
        {"length": 1.4, "corners": [1, 2]},
        {"length": 1.3, "corners": [3, 4]},
        {"length": 1.6, "corners": [5, 6, 7, 8, 9, 10]}
    ]
))

# 9. Britain (Silverstone)
tracks.append(RaceTrack(
    name="Silverstone Circuit",
    country="United Kingdom",
    laps=52,
    lap_length_km=5.891,
    corners_left=10,
    corners_right=8,
    direction="clockwise",
    pit_stop_loss=21,
    tyre_wear=3,
    sectors=[
        {"length": 2.2, "corners": [1, 2, 3]},
        {"length": 2.1, "corners": [4, 5, 6, 7, 8, 9]},
        {"length": 1.6, "corners": [10, 11, 12, 13, 14, 15, 16, 17]}
    ]
))

# 10. Hungary
tracks.append(RaceTrack(
    name="Hungaroring",
    country="Hungary",
    laps=70,
    lap_length_km=4.381,
    corners_left=8,
    corners_right=6,
    direction="clockwise",
    pit_stop_loss=22,
    tyre_wear=4,
    sectors=[
        {"length": 1.5, "corners": [1, 2]},
        {"length": 1.3, "corners": [3, 4, 5, 6, 7, 8, 9]},
        {"length": 1.6, "corners": [10, 11, 12, 13, 14]}
    ]
))

# 11. Belgium (Spa)
tracks.append(RaceTrack(
    name="Circuit de Spa-Francorchamps",
    country="Belgium",
    laps=44,
    lap_length_km=7.004,
    corners_left=9,
    corners_right=10,
    direction="clockwise",
    pit_stop_loss=22,
    tyre_wear=3,
    sectors=[
        {"length": 2.4, "corners": [1, 2, 3, 4]},
        {"length": 2.2, "corners": [5, 6, 7, 8, 9, 10]},
        {"length": 2.4, "corners": [11, 12, 13, 14, 15, 16, 17, 18, 19]}
    ]
))

# 12. Netherlands (Zandvoort)
tracks.append(RaceTrack(
    name="Circuit Zandvoort",
    country="Netherlands",
    laps=72,
    lap_length_km=4.259,
    corners_left=7,
    corners_right=7,
    direction="clockwise",
    pit_stop_loss=21,
    tyre_wear=3,
    sectors=[
        {"length": 1.5, "corners": [1, 2, 3]},
        {"length": 1.3, "corners": [4, 5, 6, 7]},
        {"length": 1.4, "corners": [8, 9, 10, 11, 12, 13, 14]}
    ]
))

# 13. Italy (Monza)
tracks.append(RaceTrack(
    name="Monza",
    country="Italy",
    laps=53,
    lap_length_km=5.793,
    corners_left=4,
    corners_right=7,
    direction="clockwise",
    pit_stop_loss=20,
    tyre_wear=2,
    sectors=[
        {"length": 2.0, "corners": [1, 2]},
        {"length": 1.9, "corners": [3, 4, 5]},
        {"length": 1.9, "corners": [6, 7, 8, 9, 10, 11]}
    ]
))

# 14. Singapore
tracks.append(RaceTrack(
    name="Marina Bay Street Circuit",
    country="Singapore",
    laps=61,
    lap_length_km=4.928,
    corners_left=11,
    corners_right=12,
    direction="counterclockwise",
    pit_stop_loss=25,
    tyre_wear=4,
    sectors=[
        {"length": 1.7, "corners": [1, 2, 3]},
        {"length": 1.6, "corners": [4, 5, 6, 7, 8, 9]},
        {"length": 1.6, "corners": [10, 11, 12, 13, 14, 15, 16, 17]}
    ]
))

# 15. Japan (Suzuka)
tracks.append(RaceTrack(
    name="Suzuka International Racing Course",
    country="Japan",
    laps=53,
    lap_length_km=5.807,
    corners_left=8,
    corners_right=10,
    direction="clockwise",
    pit_stop_loss=21,
    tyre_wear=4,
    sectors=[
        {"length": 2.0, "corners": [1, 2, 3, 4, 5, 6]},
        {"length": 2.0, "corners": [7, 8, 9, 10, 11]},
        {"length": 1.8, "corners": [12, 13, 14, 15, 16, 17]}
    ]
))

# 16. USA (COTA)
tracks.append(RaceTrack(
    name="Circuit of the Americas",
    country="USA",
    laps=56,
    lap_length_km=5.513,
    corners_left=9,
    corners_right=11,
    direction="counterclockwise",
    pit_stop_loss=22,
    tyre_wear=3,
    sectors=[
        {"length": 2.0, "corners": [1, 2, 3, 4, 5, 6]},
        {"length": 1.9, "corners": [7, 8, 9, 10, 11]},
        {"length": 1.6, "corners": [12, 13, 14, 15, 16, 17, 18, 19]}
    ]
))

# 17. Mexico
tracks.append(RaceTrack(
    name="Autódromo Hermanos Rodríguez",
    country="Mexico",
    laps=71,
    lap_length_km=4.304,
    corners_left=6,
    corners_right=10,
    direction="clockwise",
    pit_stop_loss=22,
    tyre_wear=2,
    sectors=[
        {"length": 1.4, "corners": [1, 2, 3]},
        {"length": 1.5, "corners": [4, 5, 6, 7, 8]},
        {"length": 1.4, "corners": [9, 10, 11, 12, 13, 14, 15, 16]}
    ]
))

# 18. Brazil
tracks.append(RaceTrack(
    name="Interlagos",
    country="Brazil",
    laps=71,
    lap_length_km=4.309,
    corners_left=8,
    corners_right=6,
    direction="counterclockwise",
    pit_stop_loss=22,
    tyre_wear=3,
    sectors=[
        {"length": 1.5, "corners": [1, 2, 3]},
        {"length": 1.3, "corners": [4, 5, 6, 7, 8]},
        {"length": 1.5, "corners": [9, 10, 11, 12, 13, 14]}
    ]
))

# 19. Las Vegas
tracks.append(RaceTrack(
    name="Las Vegas Street Circuit",
    country="USA",
    laps=50,
    lap_length_km=6.201,
    corners_left=8,
    corners_right=9,
    direction="counterclockwise",
    pit_stop_loss=23,
    tyre_wear=2,
    sectors=[
        {"length": 2.1, "corners": [1, 2, 3]},
        {"length": 2.0, "corners": [4, 5, 6, 7, 8]},
        {"length": 2.1, "corners": [9, 10, 11, 12, 13, 14, 15]}
    ]
))

# 20. Qatar (Lusail)
tracks.append(RaceTrack(
    name="Lusail International Circuit",
    country="Qatar",
    laps=57,
    lap_length_km=5.419,
    corners_left=6,
    corners_right=10,
    direction="clockwise",
    pit_stop_loss=22,
    tyre_wear=4,
    sectors=[
        {"length": 2.0, "corners": [1, 2, 3]},
        {"length": 1.8, "corners": [4, 5, 6, 7, 8, 9]},
        {"length": 1.6, "corners": [10, 11, 12, 13, 14, 15, 16]}
    ]
))

# 21. Abu Dhabi
tracks.append(RaceTrack(
    name="Yas Marina Circuit",
    country="UAE",
    laps=58,
    lap_length_km=5.281,
    corners_left=6,
    corners_right=10,
    direction="clockwise",
    pit_stop_loss=22,
    tyre_wear=3,
    sectors=[
        {"length": 1.9, "corners": [1, 2, 3]},
        {"length": 1.8, "corners": [4, 5, 6, 7, 8]},
        {"length": 1.6, "corners": [9, 10, 11, 12, 13, 14, 15]}
    ]
))


# Debug: Print all tracks
if __name__ == "__main__":
    for track in tracks:
        print(track)
