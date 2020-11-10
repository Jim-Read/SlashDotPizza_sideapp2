from main import ma
from models.Users import Users

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

user_schema = UserSchema()
users_schema = UserSchema(many=True)