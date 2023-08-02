from flask import *
import os
from flask import request
from flask import jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.debug = True
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)
TEMPLATES_AUTO_RELOAD = True


@app.route('/')
def home():

    ip = request.remote_addr

    return render_template('index.html', ip=ip)


@app.route("/txt", methods=["GET"])
def get_ip():

    ip = request.remote_addr

    return ip, 200
    

@app.route("/json", methods=["GET"])
def json_ip():

    ip = request.remote_addr

    return jsonify({'ip': ip}), 200


@app.route('/test')
def test():

    ip = request.remote_addr

    return render_template('index-test.html', ip=ip)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=4000)