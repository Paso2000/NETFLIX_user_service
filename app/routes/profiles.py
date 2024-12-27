from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_profile

# Define the Blueprint
profiles_bp = Blueprint("profiles", __name__)

@profiles_bp.route("/<int:userId>/profiles", methods=["GET"])
def get_profiles(userId):
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404

    profiles = list(mongo.db.profiles.find({"userId": userId}))
    for profile in profiles:
        profile["_id"] = str(profile["_id"])
    return jsonify(profiles), 200

@profiles_bp.route("/<int:userId>/profiles", methods=["POST"])
def add_profile(userId):
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    valid, error = validate_profile(data)
    if not valid:
        return jsonify(error), 400

    data["userId"] = userId
    mongo.db.profiles.insert_one(data)
    return jsonify({"message": "Profile added successfully"}), 201

@profiles_bp.route("/<int:userId>/profiles/profile<int:profileId>", methods=["GET"])
def get_profile(userId, profileId):
    profile = mongo.db.profiles.find_one({"userId": userId, "profileId": profileId})
    if profile:
        profile["_id"] = str(profile["_id"])
        return jsonify(profile), 200
    return jsonify({"error": "Profile not found"}), 404

@profiles_bp.route("/<int:userId>/profiles/profile<int:profileId>", methods=["PUT"])
def update_profile(userId, profileId):
    data = request.json
    updated_profile = mongo.db.profiles.find_one_and_update(
        {"userId": userId, "profileId": profileId},
        {"$set": data},
        return_document=True
    )
    if updated_profile:
        updated_profile["_id"] = str(updated_profile["_id"])
        return jsonify(updated_profile), 200
    return jsonify({"error": "Profile not found"}), 404

@profiles_bp.route("/<int:userId>/profiles/profile<int:profileId>", methods=["DELETE"])
def delete_profile(userId, profileId):
    result = mongo.db.profiles.delete_one({"userId": userId, "profileId": profileId})
    if result.deleted_count > 0:
        return "", 204
    return jsonify({"error": "Profile not found"}), 404
