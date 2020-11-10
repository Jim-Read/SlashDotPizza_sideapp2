from models.Favfriends import Favfriends
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.FavfriendsSchema import favfriend_schema_schema, favfriends_schema_schema

users_friends = Blueprint('users_friends', __name__,url_prefix="/users_friends")
add_friend = Blueprint('add_friend', __name__,url_prefix="/users_friends")


@users_friends.route("/", methods=["GET"])
def friend_index():
    #Return all users friends
    friends = Favfriends.query.all()
    return jsonify(friends_schema.dump(friends))


@users_friends.route("/add_friend", methods=['GET', 'POST'])
def friend_create():
    #Add a new friend
    friend_fields = friend_schema.load(request.json)
    new_friend = Favfriends()
    new_friend.title = user_fields["user_id"]
    new_friend.title = user_fields["users_friend"]   
    db.session.add(new_friend)
    db.session.commit()   
    return jsonify(friend_schema.dump(new_friend))

@users_friends.route("/<int:id>", methods=["GET"])
def user_friendshow(id):
    #Return a friend
    friend = Favfriends.query.get(id)
    return jsonify(friend_schema.dump(friend))

@users_friends.route("/<int:id>", methods=["DELETE"])
def del_favuser(id):
    #Delete a friend
    friend = Favfriends.query.get(id)
    db.session.delete(friend)
    db.session.commit()
    return jsonify(friend_schema.dump(friend))