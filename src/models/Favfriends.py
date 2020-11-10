from main import db

class Favfriends(db.Model):
    __tablename__  =  "fav_friends"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())