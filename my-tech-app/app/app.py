import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

app_version = os.environ.get('APP_VERSION', '1.0.0')
hostname = socket.gethostname()

@app.route('/')
def get_info():
    data = {
        'message': 'Welcome to My Tech App! 🚀',
        'version': app_version,
        'hostname': hostname
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)