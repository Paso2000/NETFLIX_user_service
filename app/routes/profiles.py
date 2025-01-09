from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_profile

"""
Blueprint for profile-related API routes.


Endpoints
---------
GET /users/<userId>/profiles:
    Retrieve all profiles associated with a specific user.

POST /users/<userId>/profiles:
    Add a new profile to a specific user and update their profile list.

GET /users/<userId>/profiles/<profileId>:
    Retrieve a specific profile for a user by its profileId.

PUT /users/<userId>/profiles/<profileId>:
    Update a specific profile for a user by its profileId.

DELETE /users/<userId>/profiles/<profileId>:
    Delete a specific profile for a user and update their profile list.
"""

profiles_bp = Blueprint("users", __name__)


@profiles_bp.route("/<int:userId>/profiles", methods=["GET"])
def get_profiles(userId):
    """
    Retrieve all profiles associated with a specific user.

    Parameters
    ----------
    userId : int
        The unique identifier of the user.

    Returns
    -------
    Response
        - 200: List of profiles for the user.
        - 404: User not found error.
    """
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404

    profiles = list(mongo.db.profiles.find({"userId": userId}))
    for profile in profiles:
        profile["_id"] = str(profile["_id"])  # Converti ObjectId in stringa
    return jsonify(profiles), 200


@profiles_bp.route("/<int:userId>/profiles", methods=["POST"])
def add_profile(userId):
    """
   Add a new profile to a specific user and update their profile list.

   Parameters
   ----------
   userId : int
       The unique identifier of the user.

   Request Body
   ------------
   JSON
       The details of the new profile.

   Returns
   -------
   Response
       - 201: Profile added and user updated successfully.
       - 404: User not found error.
       - 400: Validation error.
   """

    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    valid, error = validate_profile(data)
    if not valid:
        return jsonify(error), 400

    data["userId"] = userId
    mongo.db.profiles.insert_one(data)
    existing_profiles = user.get("profiles", "")
    new_profiles = f"{existing_profiles}, {data['profileId']}".strip(", ")
    mongo.db.users.update_one({"userId": userId}, {"$set": {"profiles": new_profiles}})
    return jsonify({"message": "Profile added and user updated successfully"}), 201


@profiles_bp.route("/<int:userId>/profiles/<int:profileId>", methods=["GET"])
def get_profile(userId, profileId):
    """
    Retrieve a specific profile for a user by its profileId.

    Parameters
    ----------
    userId : int
        The unique identifier of the user.
    profileId : int
        The unique identifier of the profile.

    Returns
    -------
    Response
        - 200: Profile details if found.
        - 404: User or profile not found error.
    """
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404

    profile = mongo.db.profiles.find_one({"userId": userId, "profileId": profileId})
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    profile["_id"] = str(profile["_id"])
    return jsonify(profile), 200


@profiles_bp.route("/<int:userId>/profiles/<int:profileId>", methods=["PUT"])
def update_profile(userId, profileId):
    """
    Update a specific profile for a user by its profileId.

    Parameters
    ----------
    userId : int
        The unique identifier of the user.
    profileId : int
        The unique identifier of the profile.

    Request Body
    ------------
    JSON
        The updated profile details.

    Returns
    -------
    Response
        - 200: Updated profile details.
        - 404: Profile not found error.
    """

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


@profiles_bp.route("/<int:userId>/profiles/<int:profileId>", methods=["DELETE"])
def delete_profile(userId, profileId):
    """
    Delete a specific profile for a user and update their profile list.

    Parameters
    ----------
    userId : int
        The unique identifier of the user.
    profileId : int
        The unique identifier of the profile.

    Returns
    -------
    Response
        - 204: Profile deleted successfully.
        - 404: User or profile not found error.
    """

    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404

    result = mongo.db.profiles.delete_one({"profileId": profileId, "userId": userId})
    if result.deleted_count == 0:
        return jsonify({"error": "Profile not found"}), 404

    existing_profiles = user.get("profiles", "").split(", ")
    updated_profiles = [p for p in existing_profiles if p != str(profileId)]
    mongo.db.users.update_one({"userId": userId}, {"$set": {"profiles": ", ".join(updated_profiles)}})
    return jsonify({"message": "Profile deleted and user updated successfully"}), 204
