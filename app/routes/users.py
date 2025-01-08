from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_user

"""
Blueprint for user-related API routes.

Endpoints
---------
GET /users:
    Retrieve a list of all users.

POST /users:
    Create a new user and initialize it with a default profile.

GET /users/<userId>:
    Retrieve details of a specific user by their userId.

PUT /users/<userId>:
    Update details of a specific user by their userId.

DELETE /users/<userId>:
    Delete a specific user and all associated profiles by their userId.
"""

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["GET"])
def get_users():
    """
    Retrieve a list of all users.

    Returns
    -------
    Response
        JSON response containing a list of all users.
    """
    users = list(mongo.db.users.find())
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string for serialization
    return jsonify(users), 200


@users_bp.route("/", methods=["POST"])
def add_user():
    """
   Create a new user and initialize it with a default profile.

   Request Body
   ------------
   JSON
       The details of the new user.

   Returns
   -------
   Response
       - 201: User and default profile created successfully.
       - 400: Validation error.
   """
    data = request.json
    valid, error = validate_user(data)
    if not valid:
        return jsonify(error), 400
    initial_profile = {
        "profileId": 1,  # Profilo predefinito
        "userId": data["userId"],  # Associa il profilo all'utente
        "profileImage": "/sfondo1.png",  # Profilo immagine di default
        "nickname": "Default Profile"
    }
    data["profiles"] = "1"
    mongo.db.users.insert_one(data)
    mongo.db.profiles.insert_one(initial_profile)
    return jsonify({"message": "User and initial profile added successfully"}), 201


@users_bp.route("/<int:userId>", methods=["GET"])
def get_user_by_id(userId):
    """
    Retrieve details of a specific user by their userId.

    Args:
        userId (int): The unique ID of the user.

    Returns:
        Response:
            - 200: User details if found.
            - 404: Error message if the user is not found.
    """
    user = mongo.db.users.find_one({"userId": userId})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@users_bp.route("/<int:userId>", methods=["PUT"])
def update_user(userId):
    """
    Update details of a specific user by their userId.

    Args:
        userId (int): The unique ID of the user.

    Request Body:
        JSON: Updated user details.

    Returns:
        Response:
            - 200: Updated user details if successful.
            - 404: Error message if the user is not found.
    """
    data = request.json
    updated_user = mongo.db.users.find_one_and_update(
        {"userId": userId},
        {"$set": data},
        return_document=True
    )
    if updated_user:
        updated_user["_id"] = str(updated_user["_id"])
        return jsonify(updated_user), 200
    return jsonify({"error": "User not found"}), 404


@users_bp.route("/<int:userId>", methods=["DELETE"])
def delete_user(userId):
    """
    Delete a specific user by their userId.

    Args:
        userId (int): The unique ID of the user.

    Returns:
        Response:
            - 204: No content if deletion is successful.
            - 404: Error message if the user is not found.
    """
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404

    user_result = mongo.db.users.delete_one({"userId": userId})
    profiles_result = mongo.db.profiles.delete_many({"userId": userId})

    return jsonify({
        "message": "User and associated profiles deleted successfully",
        "deleted_user_count": user_result.deleted_count,
        "deleted_profiles_count": profiles_result.deleted_count
    }), 200
