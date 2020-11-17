from main import ma
from models.PizzaImage import PizzaImage
from marshmallow.validate import Length

class PizzaImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PizzaImage
    
    filename = ma.String(required=True, validate=Length(min=1))

pizza_image_schema = PizzaImageSchema()