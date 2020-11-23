from main import db

class PizzaRating(db.Model):
    __tablename__ = "pizza_rating"
    
    rating_id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer())
    user_rating = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.pizza_id"), nullable=False)

    def __repr__(self):
        return f"<{self.user_id} rated {self.pizza_id} = {self.user_rating}>"