from models.FavFriends import FavFriends
from models.User import User
from main import db
from schemas.FavFriendsSchema import favfriend_schema, favfriends_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

fav_friends = Blueprint('fav_friends', __name__, url_prefix="/users/<int:user_id>/fav_friends")

@fav_friends.route("/", methods=["GET"])
def friend_index():
    #Retrieve all friends
    fav_friends = FavFriends.query.options(joinedload("user")).all()
    return jsonify(favfriends_schema.dump(fav_friends))
