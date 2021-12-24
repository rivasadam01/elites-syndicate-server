from flask import Flask
from flask_cors import CORS
from os import path

basedir = path.abspath(path.dirname(__file__))
cert = path.join(basedir, 'cert')

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6660, ssl_context=(
        path.join(cert, 'cert.pem'), path.join(cert, 'key.pem')), debug=True)
