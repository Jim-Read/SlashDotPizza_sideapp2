from main import db
from models.PizzaImage import PizzaImage

class Pizza(db.Model):
    __tablename__ = "pizzas"
    
    pizza_id = db.Column(db.Integer, primary_key=True)
    pizza_name = db.Column(db.String())
    description = db.Column(db.String())
    price = db.Column(db.Integer())
    location = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    pizza_image = db.relationship("PizzaImage", backref="pizza", uselist=False)

    def __repr__(self):
        return f"<pizza = {self.pizza_image}\n{self.pizza_name}\n{self.price}\n{self.description}\n{self.location}>"