from models.Pizza import Pizza
from models.User import User
from main import db
from schemas.PizzaSchema import pizza_schema, pizzas_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

pizzas = Blueprint('pizzas', __name__, url_prefix="/pizzas")

@pizzas.route("/", methods=["GET"])
def pizza_index():
    #Retrieve all pizzas
    pizzas = Pizza.query.options(joinedload("user")).all()
    return jsonify(pizzas_schema.dump(pizzas))

@pizzas.route("/", methods=["POST"])
@jwt_required
@verify_user
def pizza_create(user=None):
    #Create a new pizza
    pizza_fields = pizza_schema.load(request.json)

    new_pizza = Pizza()
    new_pizza.pizza_name = pizza_fields["pizza_name"]
    new_pizza.description = pizza_fields["description"]
    new_pizza.price = pizza_fields["price"]
    new_pizza.location = pizza_fields["location"]

    user.pizzas.append(new_pizza)

    db.session.commit()
    
    return jsonify(pizza_schema.dump(new_pizza))

@pizzas.route("/<int:id>", methods=["GET"])
def pizza_show(id):
    #Return a single pizza
    pizza = Pizza.query.get(id)
    return jsonify(pizza_schema.dump(pizza))

@pizzas.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def pizza_update(id, user=None):
    #Update a pizza
    pizza_fields = pizza_schema.load(request.json)

    pizzas = Pizza.query.filter_by(pizza_id=id, user_id=user.user_id)

    if pizzas.count() != 1:
        return abort(401,  description="Unauthorized to update this pizza")    
    
    pizzas.update(pizza_fields)
    db.session.commit()

    return jsonify(pizza_schema.dump(pizzas[0]))

@pizzas.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def pizza_delete(id, user=None):
    #Delete a pizza

    pizza = Pizza.query.filter_by(pizza_id=id, user_id=user.user_id).first()

    if not pizza:
        return abort(400)
    
    db.session.delete(pizza)
    db.session.commit()

    return jsonify(pizza_schema.dump(pizza))