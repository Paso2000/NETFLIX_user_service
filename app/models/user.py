class User:

    def __init__(self, userId: int, name: str, surname: str, password: str, email: str,
                 date_of_birth: str, paymentMethod : str, profiles: str):
        self.userId : userId
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.date_of_birth = date_of_birth
        self.paymentMethod = paymentMethod
        self.profiles = profiles

    def to_dict(self):
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
