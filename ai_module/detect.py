# detect.py
# Simple traffic detection logic for hackathon demo

import random

def detect_traffic():
    """
    Simulates vehicle detection and traffic density
    """

    # Simulate vehicle count (fake but realistic)
    vehicle_count = random.randint(5, 60)

    # Decide traffic density
    if vehicle_count < 15:
        density = "Low"
        signal_time = 20   # seconds
    elif vehicle_count < 35:
        density = "Medium"
        signal_time = 40
    else:
        density = "High"
        signal_time = 60

    return {
        "vehicle_count": vehicle_count,
        "traffic_density": density,
        "signal_time": signal_time
    }


# Run this file directly for testing
if __name__ == "__main__":
    result = detect_traffic()
    print("Traffic Analysis Result")
    print("-----------------------")
    print("Vehicle Count:", result["vehicle_count"])
    print("Traffic Density:", result["traffic_density"])
    print("Green Signal Time:", result["signal_time"], "seconds")
