from main import db

class Favpizza(db.Model):
    __tablename__  =  "fav_pizza"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())