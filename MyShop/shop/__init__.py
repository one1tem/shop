from flask import Flask

app = Flask(__name__)

# registriere die Datei routes.py
from shop.routes import home, register

