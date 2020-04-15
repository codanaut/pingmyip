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

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return render_template('index.html', ip=ip)


@app.route("/txt", methods=["GET"])
def get_ip():

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return ip, 200
    

@app.route("/json", methods=["GET"])
def json_ip():

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return jsonify({'ip': ip}), 200

@app.route('/test')
def test():

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return render_template('index.html', ip=ip)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=4000)