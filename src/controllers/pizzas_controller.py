from models.Pizza import Pizza
from main import db
from schemas.PizzaSchema import pizza_schema, pizzas_schema
from flask import Blueprint, request, jsonify, abort
pizzas = Blueprint('pizzas', __name__, url_prefix="/pizzas")

@pizzas.route("/", methods=["GET"])
def pizza_index():
    #Retrieve all pizzas
    pizzas = Pizza.query.all()
    return jsonify(pizzas_schema.dump(pizzas))

@pizzas.route("/", methods=["POST"])
def pizza_create():
    #Create a new pizza
    pizza_fields = pizza_schema.load(request.json)

    new_pizza = Pizza()
    new_pizza.title = pizza_fields["pizza_name"]
    new_pizza.title = pizza_fields["description"]
    new_pizza.title = pizza_fields["price"]
    new_pizza.title = pizza_fields["location"]
    new_pizza.title = pizza_fields["pizza_image"]
    
    
    db.session.add(new_pizza)
    db.session.commit()
    
    return (jsonify(pizza_schema.dump(new_pizza)), 200)

@pizzas.route("/<int:pizza_id>", methods=["GET"])
def pizza_show(pizza_id):
    #Return a single pizza
    pizza = Pizza.query.get(pizza_id)
    return jsonify(pizza_schema.dump(pizza))

@pizzas.route("/<int:pizza_id>", methods=["PUT", "PATCH"])
def pizza_update(pizza_id):
    #Update a pizza
    pizzas = Pizza.query.filter_by(pizza_id=pizza_id)
    pizza_fields = pizza_schema.load(request.json)
    pizzas.update(pizza_fields)
    db.session.commit()

    return jsonify(pizza_schema.dump(pizzas[0]))

@pizzas.route("/<int:pizza_id>", methods=["DELETE"])
def pizza_delete(pizza_id):
    #Delete a pizza
    pizza = Pizza.query.get(pizza_id)
    db.session.delete(pizza)
    db.session.commit()

    return jsonify(pizza_schema.dump(pizza))



    #     $ export FLASK_APP=main.py
    # $ export FLASK_ENV=development
    # $ flask run

    # psql --host=mydbinstance.cudvrkh0olql.us-east-1.rds.amazonaws.com --port=5432 --username=jamaldiab --password --dbname=myfirstdb
    # psql --host=slashdotpizza.cwatzillm6wc.us-east-1.rds.amazonaws.com --port=5432 --username=slash --password --dbname=slashdotpizza
    #DB_URI=postgresql+psycopg2://app:Testing1@localhost:5432/library_api










































# from models.Book import Book
# from main import db
# from schemas.BookSchema import book_schema, books_schema
# from flask import Blueprint, request, jsonify, abort
# books = Blueprint('books', __name__, url_prefix="/books")

# @books.route("/", methods=["GET"])
# def book_index():
#     #Retrieve all books
#     books = Book.query.all()
#     return jsonify(books_schema.dump(books))

# @books.route("/", methods=["POST"])
# def book_create():
#     #Create a new book
#     book_fields = book_schema.load(request.json)

#     new_book = Book()
#     new_book.title = book_fields["title"]
    
#     db.session.add(new_book)
#     db.session.commit()
    
#     return (jsonify(book_schema.dump(new_book)), 200)

# @books.route("/<int:id>", methods=["GET"])
# def book_show(id):
#     #Return a single book
#     book = Book.query.get(id)
#     return jsonify(book_schema.dump(book))

# @books.route("/<int:id>", methods=["PUT", "PATCH"])
# def book_update(id):
#     #Update a book
#     books = Book.query.filter_by(id=id)
#     book_fields = book_schema.load(request.json)
#     books.update(book_fields)
#     db.session.commit()

#     return jsonify(book_schema.dump(books[0]))

# @books.route("/<int:id>", methods=["DELETE"])
# def book_delete(id):
#     #Delete a book
#     book = Book.query.get(id)
#     db.session.delete(book)
#     db.session.commit()

#     return jsonify(book_schema.dump(book))



#     #     $ export FLASK_APP=main.py
#     # $ export FLASK_ENV=development
#     # $ flask run

#     # psql --host=mydbinstance.cudvrkh0olql.us-east-1.rds.amazonaws.com --port=5432 --username=jamaldiab --password --dbname=myfirstdb
#     # psql --host=slashdotpizza.cwatzillm6wc.us-east-1.rds.amazonaws.com --port=5432 --username=slash --password --dbname=slashdotpizza
#     #DB_URI=postgresql+psycopg2://app:Testing1@localhost:5432/library_api
