from models.FavPizza import FavPizza
from models.User import User
from main import db
from schemas.FavPizzaSchema import favpizza_schema, favpizzas_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

fav_pizza = Blueprint('fav_pizz', __name__, url_prefix="/users/<int:user_id>/fav_pizza")

@fav_pizza.route("/", methods=["GET"])
def favpizza_index():
    #Retrieve all favourite pizzas for user
    fav_pizzas = FavPizza.query.options(joinedload("user")).all()
    return jsonify(favpizzas_schema.dump(fav_pizzas))
