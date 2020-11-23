from main import ma
from models.FavFriends import FavFriends
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class FavFriendsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FavFriends
    
    fav_friends_id = ma.Integer(required=True)
    user_id = ma.Integer(required=True)
    friend_id = ma.Integer(required=True)
    user = ma.Nested(UserSchema)
    
favfriend_schema = FavFriendsSchema()
favfriends_schema = FavFriendsSchema(many=True)