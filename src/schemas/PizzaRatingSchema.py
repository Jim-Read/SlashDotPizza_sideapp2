from main import ma
from models.PizzaRating import PizzaRating
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class PizzaRatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PizzaRating
    
    rating_id = ma.Integer(required=True)
    pizza_id = ma.Integer(required=True)
    user_id = ma.Integer(required=True)
    user_rating = ma.Integer(required=True)
    user = ma.Nested(UserSchema)
    
pizzarating_schema = PizzaRatingSchema()
pizzaratings_schema = PizzaRatingSchema(many=True)