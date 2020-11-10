from main import db

class Likes(db.Model):
    __tablename__  =  "likes"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())