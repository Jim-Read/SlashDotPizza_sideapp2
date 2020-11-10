from flask import Flask, request, jsonify

from database import cursor, connection

app = Flask(__name__)

from pizzas import pizzas
app.register_blueprint(pizzas)