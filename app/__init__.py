from flask import Flask
from .models import setup_db
from flask_cors import CORS

app = Flask(__name__)
setup_db(app)
CORS(app)

from app import routes