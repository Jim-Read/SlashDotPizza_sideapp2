from models.Likes import Likes
from models.User import User
from main import db
from schemas.LikesSchema import like_schema, likes_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

likes = Blueprint('likes', __name__, url_prefix="/pizzas/<int:pizza_id>/comments/<int:comment_id>/likes")

@likes.route("/", methods=["GET"])
def likes_index():
    #Retrieve all user likes on a pizza
    likes = Likes.query.options(joinedload("user")).all()
    return jsonify(likes_schema.dump(likes))
