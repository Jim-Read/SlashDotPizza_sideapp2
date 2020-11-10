from main import ma
from models.Pizzas import Pizzas

class PizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pizzas

pizza_schema = PizzaSchema()
pizzas_schema = PizzaSchema(many=True)