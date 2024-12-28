from flask import Blueprint, request, jsonify
from services.db import mongo
from utils.validation import validate_profile

# Define the Blueprint
profiles_bp = Blueprint("users", __name__)

@profiles_bp.route("/<int:userId>/profiles", methods=["GET"])
def get_profiles(userId):
    # Verifica che l'utente esista
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404
    # Recupera tutti i profili associati all'utente
    profiles = list(mongo.db.profiles.find({"userId": userId}))
    for profile in profiles:
        profile["_id"] = str(profile["_id"])  # Converti ObjectId in stringa
    return jsonify(profiles), 200

@profiles_bp.route("/<int:userId>/profiles", methods=["POST"])
def add_profile(userId):
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404
    # Dati del nuovo profilo dalla richiesta
    data = request.json
    # Validazione del profilo
    valid, error = validate_profile(data)
    if not valid:
        return jsonify(error), 400
    # Imposta l'userId sul profilo
    data["userId"] = userId
    # Inserisce il profilo nel database dei profili
    mongo.db.profiles.insert_one(data)
    # Aggiorna la lista dei profili dell'utente
    existing_profiles = user.get("profiles", "")
    new_profiles = f"{existing_profiles}, {data['profileId']}".strip(", ")
    mongo.db.users.update_one({"userId": userId}, {"$set": {"profiles": new_profiles}})

    return jsonify({"message": "Profile added and user updated successfully"}), 201

@profiles_bp.route("/<int:userId>/profiles/<int:profileId>", methods=["GET"])
def get_profile(userId, profileId):
    # Verifica che l'utente esista
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404
    # Recupera il profilo specifico
    profile = mongo.db.profiles.find_one({"userId": userId, "profileId": profileId})
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    # Converti l'ObjectId in stringa per la serializzazione
    profile["_id"] = str(profile["_id"])

    return jsonify(profile), 200

@profiles_bp.route("/<int:userId>/profiles/<int:profileId>", methods=["PUT"])
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

@profiles_bp.route("/<int:userId>/profiles/<int:profileId>", methods=["DELETE"])
def delete_profile(userId, profileId):
    # Verifica che l'utente esista
    user = mongo.db.users.find_one({"userId": userId})
    if not user:
        return jsonify({"error": "User not found"}), 404
    # Elimina il profilo dal database dei profili
    result = mongo.db.profiles.delete_one({"profileId": profileId, "userId": userId})
    if result.deleted_count == 0:
        return jsonify({"error": "Profile not found"}), 404
    # Aggiorna la lista dei profili dell'utente
    existing_profiles = user.get("profiles", "").split(", ")
    updated_profiles = [p for p in existing_profiles if p != str(profileId)]
    mongo.db.users.update_one({"userId": userId}, {"$set": {"profiles": ", ".join(updated_profiles)}})
    return jsonify({"message": "Profile deleted and user updated successfully"}), 204



