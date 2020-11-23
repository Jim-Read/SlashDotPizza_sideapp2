from main import db

class FavFriends(db.Model):
    __tablename__ = "fav_friends"
    
    fav_friends_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String())
    friend_id = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self):
        return f"<friend {self.user_id}>"