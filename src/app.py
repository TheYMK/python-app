from flask import Flask, jsonify
import datetime
import socket



app = Flask(__name__)

@app.route("/api/v1/details")
def details():
    ts = datetime.datetime.now()
    hn = socket.gethostname()
    return jsonify(
        {
            'title': 'Hello Kaym Kassai',
            'time': ts,
            'hostname': hn,
            'version': "v1.0.5"
        }
    )

@app.route("/api/v1/healthz")
def health():
    return jsonify(
        {
            'status': 'up'
        }
    ), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# '/api/v1/details'
# '/api/v1/healthz'

