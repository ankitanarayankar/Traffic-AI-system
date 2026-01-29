# app.py
# Backend API for Traffic Analysis System (with CORS enabled)

from flask import Flask, jsonify
from flask_cors import CORS
import sys
import os

# Add ai_module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_module.detect import detect_traffic

app = Flask(__name__)
CORS(app)   # <<< THIS LINE FIXES YOUR ERROR

@app.route("/")
def home():
    return "Traffic AI Backend is running!"

@app.route("/traffic", methods=["GET"])
def get_traffic_data():
    result = detect_traffic()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
