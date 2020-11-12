from main import ma
from models.Pizza import Pizza
from marshmallow.validate import Length

class PizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pizza
    
    pizza_name = ma.String(required=True, validate=Length(min=1))
    description = ma.String(required=True, validate=Length(min=1))
    price = ma.String(required=True, validate=Length(min=1))
    location = ma.String(required=True, validate=Length(min=1))
    pizza_image = ma.String(required=True, validate=Length(min=1))

pizza_schema = PizzaSchema()
pizzas_schema = PizzaSchema(many=True)