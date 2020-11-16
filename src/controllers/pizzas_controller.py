from models.Pizza import Pizza
from main import db
from schemas.PizzaSchema import pizza_schema, pizzas_schema
from flask import Blueprint, request, jsonify, abort
pizzas = Blueprint('pizzas', __name__, url_prefix="/pizzas")


#Retrieve all pizzas

@pizzas.route("/", methods=["GET"])
def pizza_index():
    pizzas = Pizza.query.all()
    return jsonify(pizzas_schema.dump(pizzas))


#Create a new pizza

@pizzas.route("/", methods=["POST"])
def pizza_create():
    pizza_fields = pizza_schema.load(request.json)

    new_pizza = Pizza()
    new_pizza.pizza_name = pizza_fields["pizza_name"]
    new_pizza.description = pizza_fields["description"]
    new_pizza.price = pizza_fields["price"]
    new_pizza.location = pizza_fields["location"]
    new_pizza.pizza_image = pizza_fields["pizza_image"]
       
    db.session.add(new_pizza)
    db.session.commit()
    
    return (jsonify(pizza_schema.dump(new_pizza)), 200)


#Return a single pizza

@pizzas.route("/<int:pizza_id>", methods=["GET"])
def pizza_show(pizza_id):
    pizza = Pizza.query.get(pizza_id)
    return jsonify(pizza_schema.dump(pizza))


#Update a pizza

@pizzas.route("/<int:pizza_id>", methods=["PUT", "PATCH"])
def pizza_update(pizza_id):
    
    pizzas = Pizza.query.filter_by(pizza_id=pizza_id)
    pizza_fields = pizza_schema.load(request.json)
    pizzas.update(pizza_fields)
    db.session.commit()

    return jsonify(pizza_schema.dump(pizzas[0]))
    

#Delete a pizza

@pizzas.route("/<int:pizza_id>", methods=["DELETE"])
def pizza_delete(pizza_id):
    
    pizza = Pizza.query.get(pizza_id)
    db.session.delete(pizza)
    db.session.commit()

    return jsonify(pizza_schema.dump(pizza))