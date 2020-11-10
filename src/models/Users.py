from main import db

class Users(db.Model):
    __tablename__  =  "users"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())