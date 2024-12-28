"""
Module for data validation of user and profile objects.

Functions
---------
validate_user(data)
    Validates the structure and types of a user object.

validate_profile(data)
    Validates the structure and types of a profile object.
"""


def validate_user(data):
    """
    Validates the structure and types of a user object.

    Parameters
    ----------
    data : dict
        A dictionary representing the user object to be validated.
        Expected keys and types:
        - "userId" (int): The unique identifier for the user.
        - "name" (str): The first name of the user.
        - "surname" (str): The last name of the user.
        - "password" (str): The user's password.
        - "email" (str): The user's email address.
        - "date_of_birth" (str): The user's date of birth in the format "YYYY-MM-DD".
        - "paymentMethod" (str): The user's preferred payment method.
        - "profiles" (str): A comma-separated string of profile IDs.

    Returns
    -------
    tuple
        A tuple containing:
        - bool: True if the validation passes, False otherwise.
        - dict or None: An error message if validation fails, or None if validation passes.
    """
    required_fields = {
        "userId": int,
        "name": str,
        "surname": str,
        "password": str,
        "email": str,
        "date_of_birth": str,
        "paymentMethod": str,
        "profiles": str
    }
    # Check for missing fields
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}

    # Validate field types
    for field, field_type in required_fields.items():
        if not isinstance(data[field], field_type):
            return False, {"message": f"Field '{field}' must be of type {field_type.__name__}"}

    return True, None


def validate_profile(data):
    """
   Validates the structure and types of a profile object.

   Parameters
   ----------
   data : dict
       A dictionary representing the profile object to be validated.
       Expected keys and types:
       - "profileId" (int): The unique identifier for the profile.
       - "userId" (int): The unique identifier of the user to whom this profile belongs.
       - "profileImage" (int): An identifier for the profile image.
       - "nickname" (str): The nickname of the profile.

   Returns
   -------
   tuple
       A tuple containing:
       - bool: True if the validation passes, False otherwise.
       - dict or None: An error message if validation fails, or None if validation passes.

    """
    required_fields = {
        "profileId": int,
        "userId": int,
        "profileImage": int,
        "nickname": str
    }
    # Check for missing fields
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, {"message": f"Missing fields: {', '.join(missing_fields)}"}

    # Validate field types
    for field, field_type in required_fields.items():
        if not isinstance(data[field], field_type):
            return False, {"message": f"Field '{field}' must be of type {field_type.__name__}"}

    return True, None
