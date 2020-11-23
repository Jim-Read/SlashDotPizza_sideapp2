from main import db

class FavPizza(db.Model):
    __tablename__ = "fav_pizza"
    
    fav_pizza_id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.String())
    user_id = db.Column(db.String())

    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.pizza_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)


    def __repr__(self):
        return f"<pizza {self.pizza_id}>"