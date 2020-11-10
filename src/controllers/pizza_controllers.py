from models.Pizzas import Pizzas
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.PizzaSchema import pizzas_schema, pizza_schema

pizzas = Blueprint('pizzas', __name__, url_prefix="/pizzas")
new_pizza = Blueprint('new_pizza', __name__, url_prefix="/pizzas/")


@pizzas.route("/", methods=["GET"])
def pizza_index():
    #Return all pizzas
    pizzas = Pizzas.query.all()
    return jsonify(pizzas_schema.dump(pizzas))


@pizzas.route("/new_pizza", methods=['GET', 'POST'])
def pizza_create():
    #Create a new pizza
    pizza_fields = pizza_schema.load(request.json)
    new_pizza = Pizzas()
    new_pizza.title = pizza_fields["pizza_name"]
    new_pizza.title = pizza_fields["description"]
    new_pizza.title = pizza_fields["price"]
    new_pizza.title = pizza_fields["location"]
    new_pizza.title = pizza_fields["pizza_image"]   
    db.session.add(new_pizza)
    db.session.commit()    
    return jsonify(pizza_schema.dump(new_pizza))


@pizzas.route("/<int:id>", methods=["GET"])
def pizza_show(id):
    #Return a single pizza
    pizza = Pizzas.query.get(id)
    return jsonify(pizza_schema.dump(pizza))
    

@pizzas.route("/<int:id>", methods=["PUT", "PATCH"])
def pizza_update(id):
    #Update a pizza
    pizzas = Pizzas.query.filter_by(id=id)
    pizza_fields = pizza_schema.load(request.json)
    pizzas.update(pizza_fields)
    db.session.commit()
    return jsonify(book_schema.dump(pizzas[0]))


@pizzas.route("/<int:id>", methods=["DELETE"])
def del_pizza(id):
    #Delete a pizza
    pizza = Pizzas.query.get(id)
    db.session.delete(pizza)
    db.session.commit()
    return jsonify(pizza_schema.dump(pizza))