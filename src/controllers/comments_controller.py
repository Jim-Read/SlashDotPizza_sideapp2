from models.Comments import Comments
from models.User import User
from main import db
from schemas.CommentsSchema import comment_schema, comments_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

comments = Blueprint('comments', __name__, url_prefix="/pizzas/<int:pizza_id>/comments")

@comments.route("/", methods=["GET"])
def comments_index():
    #Retrieve all user comments
    comments = Comments.query.options(joinedload("user")).all()
    return jsonify(comments_schema.dump(comments))
