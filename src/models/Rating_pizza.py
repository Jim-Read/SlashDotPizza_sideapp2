from main import db

class Rating_pizza(db.Model):
    __tablename__  =  "pizza_rating"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())