from main import db

class PizzaImage(db.Model):
    __tablename__ = "pizza_images"

    image_id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String())
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.pizza_id"), nullable=False)

    def __repr__(self):
        return f"<PizzaImage {self.filename}>"