from flask import Flask, render_template
from tracks import tracks

simul8 = Flask(__name__) 

@simul8.route("/")
def index():
    return render_template("index.html", tracks=tracks)

if __name__ == "__main__":
    simul8.run(debug=True)
