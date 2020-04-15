from flask import *
import requests
import json
import random
import os
from flask import request
from flask import jsonify
#urls



app = Flask(__name__)
app.debug = True
TEMPLATES_AUTO_RELOAD = True


@app.route('/')
def home():

    ip = request.remote_addr

    return render_template('index.html', ip=ip)


@app.route("/txt", methods=["GET"])
def get_ip():
    return request.remote_addr, 200

@app.route("/json", methods=["GET"])
def json_ip():
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=4000)