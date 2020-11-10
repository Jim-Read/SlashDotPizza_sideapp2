from models.Favpizza import Favpizza
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.FavpizzaSchema import favpizza_schema, favpizzas_schema

users_favpizzas = Blueprint('users_favpizzas', __name__,url_prefix="/users_favpizzas")
add_pizza = Blueprint('add_pizza', __name__,url_prefix="/users_favpizzas")


@users_favpizzas.route("/", methods=["GET"])
def favpizza_index():
    #Return all favourite pizzas
    favpizzas = Favpizza.query.all()
    return jsonify(favpizzas_schema.dump(favpizzas))


@users_favpizzas.route("/add_pizza", methods=['GET', 'POST'])
def favpizza_create():
    #Add a new fav pizza
    favpizzas_fields = favpizza_schema.load(request.json)
    favpizzas_pizza = Favpizza()
    favpizzas_pizza.title = pizza_fields["user_id"]
    favpizzas_pizza.title = pizza_fields["pizza_id"]   
    db.session.add(favpizzas_pizza)
    db.session.commit()  
    return jsonify(favpizzas_schema.dump(favpizzas_pizza))


@users_favpizzas.route("/<int:id>", methods=["GET"])
def user_friendshow(id):
    #Return a fav pizza
    favpizza = Favpizza.query.get(id)
    return jsonify(favpizza_schema.dump(favpizza))


@users_favpizzas.route("/<int:id>", methods=["DELETE"])
def del_favuser(id):
    #Delete a fav pizza
    favpizza = Favpizza.query.get(id)
    db.session.delete(favpizza)
    db.session.commit()
    return jsonify(favpizza_schema.dump(favpizza))