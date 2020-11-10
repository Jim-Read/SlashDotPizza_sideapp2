from main import ma
from models.Rating_pizza import Rating_pizza

class CommentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating_pizza

ratingpizza_schema = CommentsSchema()
ratingpizzas_schema = CommentsSchema(many=True)