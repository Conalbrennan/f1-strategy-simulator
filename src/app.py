from flask import Flask, render_template, request, jsonify
from tracks import tracks
from strategy import get_lap_times, overall_stint_time, find_optimal_strategy

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
        "Tyre Wear (1–5)": track.tyre_wear,
        "Fun Facts": track.fun_facts
    }

    return jsonify(track_data)

@simul8.route("/calculate_stint", methods=["POST"])
def calculate_stint():
    data = request.json
    track = data["track"]
    tyre = data["tyre"]
    laps = int(data["laps"])
    lap_times = get_lap_times(track, tyre, laps)
    total = overall_stint_time(lap_times)
    return jsonify({
        "lap_times": lap_times,
        "total_time_sec": total,
        "total_time_str": f"{int(total // 60)}m {total % 60:.2f}s"
    })

@simul8.route("/get_optimal_strategy", methods=["POST"])
def get_optimal_strategy():
    data = request.json
    track = data["track"]
    weather = data["weather"]

    try:
        strategy, total_time, pit_loss = find_optimal_strategy(track, weather)
        return jsonify({
            "strategy": strategy,
            "total_time": total_time,
            "pit_loss": pit_loss
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    simul8.run(debug=True)
