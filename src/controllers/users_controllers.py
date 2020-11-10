from models.Users import Users
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.UserSchema import user_schema, users_schema

users = Blueprint('users', __name__, url_prefix="/users")
new_user = Blueprint('new_user', __name__, url_prefix="/users")
user_login = Blueprint('user_login', __name__, url_prefix="/")
user_logout = Blueprint('user_logout', __name__, url_prefix="/")


@users.route("/user_login", methods=["GET"])
def user_login():
    #Logs a user in
    pass


@users.route("/user_logout", methods=["GET"])
def user_logout():
    #Logs a user in
    pass


@users.route("/", methods=["GET"])
def user_index():
    #Return all users
    users = Users.query.all()
    return jsonify(users_schema.dump(users))


@users.route("/new_user", methods=['GET', 'POST'])
def user_create():
    #Create a new user
    user_fields = user_schema.load(request.json)
    new_user = Users() 
    new_user.title = user_fields["user_name"]
    new_user.title = user_fields["user_password"] 
    new_user.title = user_fields["email"]
    new_user.title = user_fields["brag"]
    new_user.title = user_fields["user_image"]
    new_user.title = user_fields["location"]   
    db.session.add(new_user)
    db.session.commit()   
    return jsonify(user_schema.dump(new_user))


@users.route("/<int:id>", methods=["GET"])
def user_show(id):
    #Return a single user
    user = Users.query.get(id)
    return jsonify(user_schema.dump(user))


@users.route("/<int:id>", methods=["PUT", "PATCH"])
def user_update(id):
    #Update a user
    users = Users.query.filter_by(id=id)
    user_fields = user_schema.load(request.json)
    users.update(user_fields)
    db.session.commit()
    return jsonify(book_schema.dump(users[0]))


@users.route("/<int:id>", methods=["DELETE"])
def del_user(id):
    #Delete a user
    user = Users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))