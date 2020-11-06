from main import db

class Book(db.Model):
    __tablename__  =  "test"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())