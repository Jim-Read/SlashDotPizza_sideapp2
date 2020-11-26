from main import db
from models.UserImage import UserImage

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    user_name = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    user_image = db.relationship("UserImage", backref="users", uselist=False)

    def __repr__(self):
        return f"<User {self.email}>"