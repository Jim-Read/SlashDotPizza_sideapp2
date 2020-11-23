from main import ma
from models.FavPizza import FavPizza
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class FavPizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FavPizza
    
    fav_pizza_id = ma.Integer(required=True)
    user_id = ma.Integer(required=True)
    pizza_id = ma.Integer(required=True)
    user = ma.Nested(UserSchema)
    
favpizza_schema = FavPizzaSchema()
favpizzas_schema = FavPizzaSchema(many=True)