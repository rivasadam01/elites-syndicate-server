from flask import Flask
from flask_cors import CORS
from os import path

basedir = path.abspath(path.dirname(__file__))
cert = path.join(basedir, '../cert')

app = Flask(__name__)
CORS(app)

import elites.routes
