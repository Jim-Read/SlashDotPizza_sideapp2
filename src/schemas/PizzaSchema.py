from main import ma
from models.Pizza import Pizza
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class PizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pizza

    pizza_name = ma.String(required=True, validate=Length(max=40))
    description = ma.String(required=True, validate=Length(max=40))
    price = ma.Integer(required=True)
    location = ma.String(required=True, validate=Length(max=40))
    recipe_image = ma.String(required=False, validate=Length(min=1))
    user = ma.Nested(UserSchema)
    
pizza_schema = PizzaSchema()
pizzas_schema = PizzaSchema(many=True)