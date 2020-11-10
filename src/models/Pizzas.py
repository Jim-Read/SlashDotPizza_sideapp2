from main import db

class Pizzas(db.Model):
    __tablename__  =  "pizzas"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())