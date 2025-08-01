class RaceTrack:
    def __init__(self, name, country, laps, lap_length_km, corners_left, corners_right,
                 direction, pit_stop_loss, tyre_wear,
                 soft_lap_time, medium_lap_time, hard_lap_time,
                 intermediate_lap_time, wet_lap_time, fun_facts):
        self.name = name
        self.country = country
        self.laps = laps
        self.lap_length_km = lap_length_km
        self.corners_left = corners_left
        self.corners_right = corners_right
        self.direction = direction
        self.pit_stop_loss = pit_stop_loss
        self.tyre_wear = tyre_wear
        self.soft_lap_time = soft_lap_time
        self.medium_lap_time = medium_lap_time
        self.hard_lap_time = hard_lap_time
        self.intermediate_lap_time = intermediate_lap_time
        self.wet_lap_time = wet_lap_time
        self.fun_facts = fun_facts

    def total_race_distance(self):
        return self.laps * self.lap_length_km

    def __repr__(self):
        return f"<RaceTrack {self.name} ({self.country}) - {self.laps} laps>"


tracks = []

tracks.append(RaceTrack(
    "Bahrain International Circuit", "Bahrain", 57, 5.412, 6, 9, "clockwise", 22, 4,
    90.0, 92.0, 94.0, 96.0, 100.0,
    [
        "Hosted the first Formula 1 race in the Middle East in 2004.",
        "Has a distinctive desert setting with night racing under floodlights.",
        "Often affected by sand on the track, impacting grip levels."
    ]
))

tracks.append(RaceTrack(
    "Jeddah Corniche Circuit", "Saudi Arabia", 50, 6.174, 11, 16, "counterclockwise", 23, 3,
    89.5, 91.5, 93.5, 95.5, 99.5,
    [
        "One of the fastest street circuits with an average speed over 250 km/h.",
        "Runs along the Red Sea coastline with sweeping high-speed corners.",
        "First used in 2021 and already known for dramatic races and safety cars."
    ]
))

tracks.append(RaceTrack(
    "Albert Park Circuit", "Australia", 58, 5.278, 7, 9, "clockwise", 21, 2,
    88.2, 90.2, 92.2, 94.2, 98.2,
    [
        "Set around a public park and lake in central Melbourne.",
        "Traditionally opens the F1 season with enthusiastic local crowds.",
        "Track surface evolves heavily over the weekend as rubber builds."
    ]
))

tracks.append(RaceTrack(
    "Imola", "Italy", 63, 4.909, 7, 12, "clockwise", 22, 3,
    88.8, 90.8, 92.8, 94.8, 98.8,
    [
        "Officially named Autodromo Enzo e Dino Ferrari.",
        "Infamous for the tragic 1994 weekend that claimed Senna and Ratzenberger.",
        "Features old-school gravel runoffs and fast, narrow corners."
    ]
))

tracks.append(RaceTrack(
    "Monaco", "Monaco", 78, 3.337, 11, 8, "clockwise", 19, 2,
    73.0, 75.0, 77.0, 79.0, 83.0,
    [
        "The most famous and glamorous race on the calendar.",
        "Overtakes are almost impossible due to the tight layout.",
        "Drivers need razor-sharp precision to avoid the barriers."
    ]
))

tracks.append(RaceTrack(
    "Circuit de Barcelona-Catalunya", "Spain", 66, 4.675, 8, 10, "clockwise", 21, 3,
    87.0, 89.0, 91.0, 93.0, 97.0,
    [
        "Used extensively for winter testing by F1 teams.",
        "Good mix of high-speed and technical corners.",
        "Usually a very high tyre wear circuit."
    ]
))

tracks.append(RaceTrack(
    "Circuit Gilles Villeneuve", "Canada", 70, 4.361, 7, 8, "clockwise", 21, 3,
    85.6, 87.6, 89.6, 91.6, 95.6,
    [
        "Named after Canadian legend Gilles Villeneuve.",
        "Features the 'Wall of Champions' at the final chicane.",
        "Unpredictable weather often plays a role in the outcome."
    ]
))

tracks.append(RaceTrack(
    "Red Bull Ring", "Austria", 71, 4.318, 3, 7, "clockwise", 20, 3,
    75.3, 77.3, 79.3, 81.3, 85.3,
    [
        "Shortest lap time on the F1 calendar.",
        "Set in the picturesque Styrian hills.",
        "Simple layout, but close racing and elevation changes add drama."
    ]
))

tracks.append(RaceTrack(
    "Silverstone Circuit", "United Kingdom", 52, 5.891, 10, 8, "clockwise", 21, 3,
    89.2, 91.2, 93.2, 95.2, 99.2,
    [
        "The birthplace of Formula 1 — first race was held here in 1950.",
        "Known for legendary corners like Maggotts and Becketts.",
        "Often has huge British crowds and changeable weather."
    ]
))

tracks.append(RaceTrack(
    "Hungaroring", "Hungary", 70, 4.381, 8, 6, "clockwise", 22, 4,
    81.7, 83.7, 85.7, 87.7, 91.7,
    [
        "Narrow, twisty track often likened to 'Monaco without the walls'.",
        "Hot and dusty conditions add to the challenge.",
        "First race behind the Iron Curtain in 1986."
    ]
))

tracks.append(RaceTrack(
    "Circuit de Spa-Francorchamps", "Belgium", 44, 7.004, 9, 10, "clockwise", 22, 3,
    104.5, 106.5, 108.5, 110.5, 114.5,
    [
        "One of the longest and most iconic circuits in F1 history.",
        "Eau Rouge-Raidillon is among the most famous corners in motorsport.",
        "Weather can vary dramatically across different sections of the track."
    ]
))

tracks.append(RaceTrack(
    "Circuit Zandvoort", "Netherlands", 72, 4.259, 7, 7, "clockwise", 21, 3,
    77.8, 79.8, 81.8, 83.8, 87.8,
    [
        "Features steep banking at the final corner for added speed.",
        "Home race for Max Verstappen, with a huge Dutch fan presence.",
        "A tight and twisty layout makes overtaking very difficult."
    ]
))

tracks.append(RaceTrack(
    "Monza", "Italy", 53, 5.793, 4, 7, "clockwise", 20, 2,
    81.5, 83.5, 85.5, 87.5, 91.5,
    [
        "Known as the 'Temple of Speed' for its long straights.",
        "Old banked sections of the track still exist but aren't used.",
        "Italian fans — the Tifosi — create a passionate race atmosphere."
    ]
))

tracks.append(RaceTrack(
    "Marina Bay Street Circuit", "Singapore", 61, 4.928, 11, 12, "counterclockwise", 25, 4,
    96.0, 98.0, 100.0, 102.0, 106.0,
    [
        "The original night race in F1, held entirely under lights.",
        "Very physically demanding due to heat and humidity.",
        "Longest race on the calendar in terms of duration."
    ]
))

tracks.append(RaceTrack(
    "Suzuka International Racing Course", "Japan", 53, 5.807, 8, 10, "clockwise", 21, 4,
    92.3, 94.3, 96.3, 98.3, 102.3,
    [
        "Only figure-eight circuit in Formula 1.",
        "Japanese fans are known for their elaborate costumes and loyalty.",
        "Drivers love it for its flowing rhythm and technical challenge."
    ]
))

tracks.append(RaceTrack(
    "Circuit of the Americas", "USA", 56, 5.513, 9, 11, "counterclockwise", 22, 3,
    90.5, 92.5, 94.5, 96.5, 100.5,
    [
        "Built specifically for F1 in Austin, Texas.",
        "Turn 1 features a steep uphill climb followed by a blind apex.",
        "Mixes elements inspired by Silverstone, Hockenheim, and others."
    ]
))

tracks.append(RaceTrack(
    "Autódromo Hermanos Rodríguez", "Mexico", 71, 4.304, 6, 10, "clockwise", 22, 2,
    80.6, 82.6, 84.6, 86.6, 90.6,
    [
        "Located at over 2,200m altitude — the highest track on the calendar.",
        "Cars run very low downforce due to thin air.",
        "The stadium section creates a spectacular atmosphere."
    ]
))

tracks.append(RaceTrack(
    "Interlagos", "Brazil", 71, 4.309, 8, 6, "counterclockwise", 22, 3,
    81.0, 83.0, 85.0, 87.0, 91.0,
    [
        "Famous for exciting races and unpredictable weather.",
        "Short lap with frequent elevation changes and cambered corners.",
        "Ayrton Senna’s emotional 1991 home win here is legendary."
    ]
))

tracks.append(RaceTrack(
    "Las Vegas Street Circuit", "USA", 50, 6.201, 8, 9, "counterclockwise", 23, 2,
    90.0, 92.0, 94.0, 96.0, 100.0,
    [
        "Returns F1 to the Las Vegas Strip with a brand-new layout.",
        "Second-ever Saturday night race since 1985.",
        "Drivers race past iconic landmarks at over 340 km/h."
    ]
))

tracks.append(RaceTrack(
    "Lusail International Circuit", "Qatar", 57, 5.419, 6, 10, "clockwise", 22, 4,
    91.5, 93.5, 95.5, 97.5, 101.5,
    [
        "Originally built for MotoGP but adapted for F1 in 2021.",
        "Wide corners allow for multiple racing lines.",
        "Located just outside Doha in the desert."
    ]
))

tracks.append(RaceTrack(
    "Yas Marina Circuit", "UAE", 58, 5.281, 6, 10, "clockwise", 22, 3,
    90.1, 92.1, 94.1, 96.1, 100.1,
    [
        "Often hosts the final race of the F1 season.",
        "Revised layout since 2021 improved overtaking opportunities.",
        "The race transitions from sunset into night under lights."
    ]
))
