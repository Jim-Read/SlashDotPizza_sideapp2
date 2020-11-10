from database import cursor, connection
from flask import Blueprint, request, jsonify
pizzas = Blueprint('pizzas', __name__, url_prefix="/pizzas")
#pizzas = Blueprint('pizzas', __name__)



@pizzas.route("/", methods=["GET"])
def pizza_index():
    #Return all books
    sql = "SELECT * FROM pizza;"
    cursor.execute(sql)
    pizza_list = cursor.fetchall()
    return jsonify(pizza_list)