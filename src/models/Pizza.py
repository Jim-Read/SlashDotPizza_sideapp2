# from main import db (Book.py)

# class Book(db.Model):
#     __tablename__ = "books"
    
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String())

from main import db

class Pizza(db.Model):
    __tablename__ = "pizzas"
    
    pizza_id = db.Column(db.Integer, primary_key=True)
    pizza_name = db.Column(db.String())
    description = db.Column(db.String())
    price = db.Column(db.String())
    location = db.Column(db.String())
    pizza_image = db.Column(db.String())