from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend running"

@app.route("/traffic")
def traffic():
    return jsonify({
        "vehicle_count": random.randint(10, 60),
        "traffic_density": "High",
        "signal_time": 60
    })

if __name__ == "__main__":
    app.run(debug=True)
