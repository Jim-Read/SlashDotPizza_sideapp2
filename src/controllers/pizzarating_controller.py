from models.PizzaRating import PizzaRating
from models.User import User
from main import db
from schemas.PizzaRatingSchema import pizzarating_schema, pizzaratings_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

pizzaratings = Blueprint('pizzaratings', __name__, url_prefix="/pizzas/<int:pizza_id>/pizza_ratings")

@pizzaratings.route("/", methods=["GET"])
def pizzaratings_index():
    #Retrieve all user pizza ratings
    pizzaratings = PizzaRating.query.options(joinedload("user")).all()
    return jsonify(pizzaratings_schema.dump(pizzaratings))

#add rating to a pizza

#view user rating for a pizza

#delete pizza rating for user