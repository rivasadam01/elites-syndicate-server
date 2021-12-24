from flask import Flask
from flask_cors import CORS
from loguru import logger
from os import path

basedir = path.abspath(path.dirname(__file__))
cert = path.join(basedir, '../cert')

app = Flask(__name__)
CORS(app)

# *The following imports must stay here
import elites.db
import elites.routes