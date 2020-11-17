from flask import Blueprint, request, jsonify, abort, current_app, Response
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
from models.PizzaImage import PizzaImage
from models.Pizza import Pizza
from schemas.PizzaImageSchema import pizza_image_schema
import boto3
from main import db
from pathlib import Path

pizza_images = Blueprint("pizza_images",  __name__, url_prefix="/pizzas/<int:pizza_id>/images")

@pizza_images.route("/", methods=["POST"])
@jwt_required
@verify_user
def pizza_image_create(pizza_id, user=None):
    pizza = Pizza.query.filter_by(pizza_id=pizza_id, user_id=user.user_id).first()

    if not pizza:
        return abort(401, description="Invalid pizza")
    
    if "image" not in request.files:
        return  abort(400, description="No Image")
    
    image = request.files["image"]

    if Path(image.filename).suffix not in [".png", ".jpeg", ".jpg", ".gif"]:
        return abort(400, description="Invalid file type")

    filename = f"{pizza_id}{Path(image.filename).suffix}"
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    key = f"pizza_images/{filename}"

    bucket.upload_fileobj(image, key)

    if not pizza.pizza_image:
        new_image = PizzaImage()
        new_image.filename = filename
        pizza.pizza_image = new_image
        db.session.commit()
    
    return ("", 201)

@pizza_images.route("/<int:id>", methods=["GET"])
def pizza_image_show(pizza_id, id):
    pizza_image = PizzaImage.query.filter_by(pizza_id=id).first()

    if not pizza_image:
        return abort(401, description="Invalid pizza")

    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    filename = pizza_image.filename
    file_obj = bucket.Object(f"pizza_images/{filename}").get()

    print(file_obj)

    return Response(
        file_obj["Body"].read(),
        mimetype="image/*",
        headers={"Content-Disposition": "attachment;filename=image"}
    )

@pizza_images.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def pizza_image_delete(pizza_id, id, user=None):
    pizza = Pizza.query.filter_by(pizza_id=id, user_id=user.user_id).first()

    if not pizza:
        return abort(401, description="Invalid pizza")
    
    if pizza.pizza_image:
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        filename = pizza.pizza_image.filename

        bucket.Object(f"pizza_images/{filename}").delete()

        db.session.delete(pizza.pizza_image)
        db.session.commit()

    return ("", 204)