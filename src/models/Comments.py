from main import db

class Comments(db.Model):
    __tablename__  =  "comments"

    id = db.Column(db.Integer,  primary_key=True)
    title  = db.Column(db.String())