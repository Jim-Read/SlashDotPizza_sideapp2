from models.Rating_pizza import Rating_pizza
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.RatingSchema import ratingpizza_schema, ratingpizzas_schema

pizza_rating = Blueprint('pizza_rating', __name__,url_prefix="/pizza_rating")
new_rating = Blueprint('new_rating', __name__,url_prefix="/pizza_rating")


@pizza_rating.route("/", methods=["GET"])
def pizza_index():
    #Return all pizza ratings by users
    pizza_rating = Rating_pizza.query.all()
    return jsonify(ratingpizza_schema.dump(pizza_rating))


@pizza_rating.route("/new_rating", methods=['GET', 'POST'])
def rating_create():
    #Create a new pizza rating
    pizzarating_fields = ratingpizza_schema.load(request.json)
    new_rating = Rating_pizza()
    new_rating.title = pizzarating_fields["user_id"]
    new_rating.title = pizzarating_fields["pizza_id"]
    new_rating.title = pizzarating_fields["user_rating"]
    db.session.add(new_rating)
    db.session.commit()  
    return jsonify(ratingpizza_schema.dump(new_rating))


@pizza_rating.route("/<int:id>", methods=["GET"])
def user_ratings(id):
    #Return a single rating
    pizza_rating = Rating_pizza.query.get(id)
    return jsonify(ratingpizza_schema.dump(pizza_rating))


@pizza_rating.route("/<int:id>", methods=["PUT", "PATCH"])
def rating_update(id):
    #Update a rating
    ratings = Rating_pizza.query.filter_by(id=id)
    pizzarating_fields = ratingpizza_schema.load(request.json)
    likes.update(pizzarating_fields)
    db.session.commit()
    return jsonify(ratingpizza_schema.dump(ratings[0]))



@pizza_rating.route("/<int:id>", methods=["DELETE"])
def del_rating(id):
    #Delete a rating
    rating_pizza = Rating_pizza.query.get(id)
    db.session.delete(rating_pizza)
    db.session.commit()
    return jsonify(ratingpizza_schema.dump(rating_pizza))