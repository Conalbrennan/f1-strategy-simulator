from flask import Flask, render_template, request, jsonify
from tracks import tracks

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

if __name__ == "__main__":
    simul8.run(debug=True)
