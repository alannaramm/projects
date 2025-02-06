from flask import Flask, jsonify
import random  # Simulating real data

app = Flask(__name__)

@app.route('/network-status')
def network_status():
    data = {
        "cpu_usage": random.randint(10, 90),  # Simulating dynamic data
        "memory_usage": random.randint(20, 80),
        "uptime": random.randint(10000, 50000)
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
