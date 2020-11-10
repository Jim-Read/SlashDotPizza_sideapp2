from models.Likes import Likes
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.LikeSchema import like_schema, likes_schema

comment_likes = Blueprint('comment_likes', __name__,url_prefix="/comment_likes")
new_like = Blueprint('new_like', __name__,url_prefix="/comment_likes")


@comment_likes.route("/", methods=["GET"])
def pizza_index():
    #Return all likes on comments
    likes = Likes.query.all()
    return jsonify(likes_schema.dump(likes))


@comment_likes.route("/new_like", methods=['GET', 'POST'])
def like_create():
    #Create a new like
    like_fields = like_schema.load(request.json)
    new_like = Likes()
    new_like.title = like_fields["comment_id"]
    new_like.title = like_fields["user_id"]
    new_like.title = like_fields["likes"]  
    db.session.add(new_like)
    db.session.commit()  
    return jsonify(like_schema.dump(new_like))
    

@comment_likes.route("/<int:id>", methods=["GET"])
def user_likes(id):
    #Return a single like
    like = Likes.query.get(id)
    return jsonify(like_schema.dump(like))


@comment_likes.route("/<int:id>", methods=["PUT", "PATCH"])
def like_update(id):
    #Update a like
    likes = Likes.query.filter_by(id=id)
    likes_fields = like_schema.load(request.json)
    likes.update(like_fields)
    db.session.commit()
    return jsonify(like_schema.dump(likes[0]))


@comment_likes.route("/<int:id>", methods=["DELETE"])
def del_likes(id):
    #Delete a like
    like = Likes.query.get(id)
    db.session.delete(like)
    db.session.commit()
    return jsonify(like_schema.dump(like))