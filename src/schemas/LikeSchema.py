from main import ma
from models.Likes import Likes

class LikeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Likes

like_schema = Likes()
likes_schema = Likes(many=True)