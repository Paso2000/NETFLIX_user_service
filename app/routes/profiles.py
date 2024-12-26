from flask import Blueprint, request, jsonify
from services.db import mongo
#from utils.validation import validate_profile

# Define the Blueprint
profiles_bp = Blueprint("profiles", __name__)

@profiles_bp.route("/", methods=["GET"])
def get_users():
    profiles = list(mongo.db.profiles.find())
    for profile in profiles:
        profile["_id"] = str(profile["_id"])  # Convert ObjectId to string for serialization
    return jsonify(profile), 200

@profiles_bp.route("/", methods=["POST"])
def add_user():
    return jsonify({"message": "Actor added successfully"}), 201
