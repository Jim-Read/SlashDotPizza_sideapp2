from main import db

class Comments(db.Model):
    __tablename__ = "comments"
    
    comment_id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer())
    comment = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.pizza_id"), nullable=False)

    def __repr__(self):
        return f"<{self.user_id} comment on {self.pizza_id} = {self.comment}>"