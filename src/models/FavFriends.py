from main import db

class FavFriends(db.Model):
    __tablename__ = "fav_friends"
    
    fav_friends_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    friend_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self):
        return f"<{self.user_id} friend/s are {self.friend_id}>"