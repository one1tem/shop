from flask import Flask

app = Flask(__name__)

# registriere die Datei routes.py
from shop import routes

