from main import ma
from models.Comments import Comments
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class CommentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comments
    
    comment_id = ma.Integer(required=True)
    pizza_id = ma.Integer(required=True)
    user_id = ma.Integer(required=True)
    comment = ma.String(required=True)
    user = ma.Nested(UserSchema)
    
comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)