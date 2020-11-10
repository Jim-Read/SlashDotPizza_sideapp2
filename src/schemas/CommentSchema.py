from main import ma
from models.Comments import Comments

class CommentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comments

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)