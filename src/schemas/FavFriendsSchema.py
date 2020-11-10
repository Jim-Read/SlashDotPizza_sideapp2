from main import ma
from models.Favfriends import Favfriends

class FavfriendsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Favfriends

favfriend_schema = FavfriendsSchema()
favfriends_schema = FavfriendsSchema(many=True)