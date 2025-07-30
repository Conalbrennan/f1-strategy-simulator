from flask import Flask, render_template, request, jsonify
from tracks import tracks
from strategy import get_lap_times, overall_stint_time

simul8 = Flask(__name__)

@simul8.route("/")
def index():
    return render_template("index.html", tracks=tracks)

@simul8.route("/get_track_data", methods=["POST"])
def get_track_data():
    track_name = request.json.get("track")
    track = next((t for t in tracks if t.name == track_name), None)

    if not track:
        return jsonify({"error": "Track not found"}), 404

    track_data = {
        "Name": track.name,
        "Country": track.country,
        "Laps": track.laps,
        "Lap Length (km)": track.lap_length_km,
        "Corners (Left)": track.corners_left,
        "Corners (Right)": track.corners_right,
        "Direction": track.direction,
        "Pit Stop Loss (s)": track.pit_stop_loss,
        "Tyre Wear (1–5)": track.tyre_wear
    }

    return jsonify(track_data)

@simul8.route("/calculate_stint", methods=["POST"])
def calculate_stint():
    data = request.json
    track_name = data.get("track")
    tyre = data.get("tyre")
    stint_laps = data.get("laps")

    try:
        lap_times = get_lap_times(track_name, tyre, stint_laps)
        total_time = overall_stint_time(lap_times)
        mins = int(total_time // 60)
        secs = total_time % 60

        return jsonify({
            "lap_times": [round(t, 2) for t in lap_times],
            "total_time_sec": total_time,
            "total_time_str": f"{mins}m {secs:.2f}s"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    simul8.run(debug=True)
