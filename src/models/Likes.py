from main import db

class Likes(db.Model):
    __tablename__ = "likes"
    
    likes_id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer())
    likes = db.Column(db.Boolean())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.comment_id"), nullable=False)

    def __repr__(self):
        return f"<{self.user_id} on {self.comment_id} = {self.likes}>"