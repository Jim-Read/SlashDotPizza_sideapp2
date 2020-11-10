from models.Comments import Comments
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.CommentSchema import comments_schema, comment_schema

pizza_comments = Blueprint('pizza_comments', __name__,url_prefix="/pizza_comments")
add_comment = Blueprint('add_comment', __name__,url_prefix="/pizza_comments")


@pizza_comments.route("/", methods=["GET"])
def pizza_index():
    #Return all comments on pizza
    comments = Comments.query.all()
    return jsonify(comments_schema.dump(comments))


@pizza_comments.route("/add_comment", methods=['GET', 'POST'])
def comment_create():
    #Create a new comment
    comment_fields = comment_schema.load(request.json)
    new_comment = Comments()
    new_comment.title = comment_fields["pizza_id"]
    new_comment.title = comment_fields["user_id"]
    new_comment.title = comment_fields["comment"]
    db.session.add(new_comment)
    db.session.commit()  
    return jsonify(comment_schema.dump(new_comment))


@pizza_comments.route("/<int:id>", methods=["GET"])
def user_comments(id):
    #Return a single comment
    comment = Comments.query.get(id)
    return jsonify(comment_schema.dump(comment))


@pizza_comments.route("/<int:id>", methods=["PUT", "PATCH"])
def comment_update(id):
    #Update a comment
    comments = Comments.query.filter_by(id=id)
    comment_fields = comment_schema.load(request.json)
    comment.update(comment_fields)
    db.session.commit()
    return jsonify(comment_schema.dump(comments[0]))


@pizza_comments.route("/<int:id>", methods=["DELETE"])
def del_comment(id):
    #Delete a comment
    comment = Comments.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify(comment_schema.dump(comment))