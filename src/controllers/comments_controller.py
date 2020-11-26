from models.Comments import Comments
from models.User import User
from main import db
from schemas.CommentsSchema import comment_schema, comments_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

comments = Blueprint('comments', __name__, url_prefix="/pizzas/comments/")

@comments.route("/", methods=["GET"])
def comments_index():
    #Retrieve all user comments
    comments = Comments.query.all()
    return jsonify(comments_schema.dump(comments))

#add comment to pizza
@comments.route("/<int:id>", methods=["POST"])
@jwt_required
@verify_user
def comment_create(pizza_id):

    comment = comment_schema.load(request.json)
    new_comment = Comments()
    new_comment.comment = comment_fields["comment"]
    new_comment.user_id = users.user_id
    new_comment.pizza_id = pizza_id
    user.comment.append(new_comment)

    db.session.commit()
    
    return jsonify(comment_schema.dump(new_comment))

#modify comment on pizza
@comments.route("/<int:comment_id>", methods=["PATCH"])
@jwt_required
@verify_user
def modify_comment(comment_id, user=None):
    comment_fields = comment_schema.load(request.json)
    comments = Comment.query.filter_by(comment_id=comment_id, user_id=user.user_id)

    if comments.count() != 1:
        return abort(401,  description="Unauthorized to update this comment")    
    
    comments.update(comment_fields)
    db.session.commit()

    return jsonify(comment_schema.dump(comments[0]))


#delete comment on pizza
@comments.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def comment_delete(pizza_id, user=None):

    comment = Comments.query.filter_by(pizza_id=pizza_id, user_id=user.user_id).first()

    if not comment:
        return abort(400, description="Unauthorized to delete this comment")
    
    db.session.delete(comment)
    db.session.commit()

    return jsonify(comment_schema.dump(comment))
