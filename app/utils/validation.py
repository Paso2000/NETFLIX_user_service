
def validate_user(data):
    required_fields = {
        "filmId": int,
        "title": str,
        "actors": str,  # Can be a comma-separated string or list
        "release_year": int,
        "genre": str,
        "rating": (int, float),  # Can be either an int or float
    }
    # Check for missing fields
    #missing_fields = [field for field in required_fields if field not in data]
    #if missing_fields:
    #    return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}

    # Validate field types
    #for field, field_type in required_fields.items():
    #    if not isinstance(data[field], field_type):
    #        return False, {"message": f"Field '{field}' must be of type {field_type.__name__}"}

    return True, None

def validate_profile(data):
    required_fields = {
        "actorId": int,
        "name": str,
        "surname": str,
        "date_of_birth": str,  # Format: "YYYY-MM-DD"
        "films": str,  # Comma-separated string
    }
    # Check for missing fields
    #missing_fields = [field for field in required_fields if field not in data]
    #if missing_fields:
    #    return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}

    # Validate field types
    #for field, field_type in required_fields.items():
    #    if not isinstance(data[field], field_type):
    #        return False, {"message": f"Field '{field}' must be of type {field_type.__name__}"}

    return True, None