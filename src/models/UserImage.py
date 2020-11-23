from main import db

class UserImage(db.Model):
    __tablename__ = "user_images"

    image_id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self):
        return f"<UserImage {self.filename}>"