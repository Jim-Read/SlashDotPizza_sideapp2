from main import ma
from models.Likes import Likes
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class LikesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Likes
    
    likes_id = ma.Integer(required=True)
    comment_id = ma.Integer(required=True)
    user_id = ma.Integer(required=True)
    likes = ma.String(required=True)
    user = ma.Nested(UserSchema)
    
like_schema = LikesSchema()
likes_schema = LikesSchema(many=True)