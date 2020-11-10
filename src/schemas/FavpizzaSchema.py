from main import ma
from models.Favpizza import Favpizza

class FavpizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Favpizza

favpizza_schema = FavpizzaSchema()
favpizzas_schema = FavpizzaSchema(many=True)