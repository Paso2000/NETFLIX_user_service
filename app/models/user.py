class User:
    """
    A class used to represent a User.

    Attributes
    ----------
    userId : int
        The unique identifier for the user.
    name : str
        The first name of the user.
    surname : str
        The last name of the user.
    password : str
        The user's password for authentication.
    email : str
        The email address of the user.
    date_of_birth : str
        The date of birth of the user in the format "YYYY-MM-DD".
    paymentMethod : str
        The preferred payment method of the user.
    profiles : str
        A comma-separated string of profile IDs associated with the user.

    Methods
    -------
    to_dict()
        Converts the User object into a dictionary representation.
    """
    def __init__(self, userId: int, name: str, surname: str, password: str, email: str, date_of_birth: str,
                 paymentMethod: str, profiles: str):
        """
        Constructs all the necessary attributes for the User object.

        Parameters
        ----------
        userId : int
            The unique identifier for the user.
        name : str
            The first name of the user.
        surname : str
            The last name of the user.
        password : str
            The user's password for authentication.
        email : str
            The email address of the user.
        date_of_birth : str
            The date of birth of the user in the format "YYYY-MM-DD".
        paymentMethod : str
            The preferred payment method of the user.
        profiles : str
            A comma-separated string of profile IDs associated with the user.
        """
        self.userId = userId
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.date_of_birth = date_of_birth
        self.paymentMethod = paymentMethod
        self.profiles = profiles

    def to_dict(self):
        """
        Converts the User object into a dictionary representation.

        Returns
        -------
        dict
            A dictionary containing the attributes of the User object.
            {
                "userId": int,
                "name": str,
                "surname": str,
                "password": str,
                "email": str,
                "date_of_birth": str,
                "paymentMethod": str,
                "profiles": str
            }
        """
        return {
            "userId" : self.userId,
            "name" : self.name,
            "surname" : self.surname,
            "password" : self.password,
            "email" : self.email,
            "date_of_birth" : self.date_of_birth,
            "paymentMethod" : self.paymentMethod,
            "profiles" : self.profiles
        }
