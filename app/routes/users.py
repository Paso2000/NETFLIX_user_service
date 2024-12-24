from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_user

# Define the Blueprint
users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def get_users():
    users = list(mongo.db.users.find())
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string for serialization
    return jsonify(users), 200

@users_bp.route("/", methods=["POST"])
def add_user():
    data = request.json
    valid, error = validate_user(data)
    if not valid:
        return jsonify(error), 400
    mongo.db.users.insert_one(data)
    return jsonify({"message": "Actor added successfully"}), 201

@users_bp.route("/<int:userId>", methods=["GET"])
def delete_actor(userId):
    return jsonify({"error": "Actor not found"}), 404
@users_bp.route("/<int:userId>", methods=["PUT"])
def delete_actor(userId):
    return jsonify({"error": "Actor not found"}), 404
@users_bp.route("/<int:userId>", methods=["DELETE"])
def delete_actor(userId):
    return jsonify({"error": "Actor not found"}), 404

