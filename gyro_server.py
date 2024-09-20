from flask import Flask, request

app = Flask(__name__)

@app.route('/gyro_data', methods=['POST'])
def gyro_data():
    data = request.json
    # Process gyro data
    # Send commands to ESP32
    return 'Received gyro data'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Run on your local network