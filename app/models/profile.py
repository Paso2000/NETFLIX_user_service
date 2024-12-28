class Profile:
    """
   A class used to represent a Profile.

   Attributes
   ----------
   profileId : int
       The unique identifier for the profile.
   userId : int
       The unique identifier of the user to whom this profile belongs.
   profileImage : int
       An identifier for the profile image associated with this profile.
   nickname : str
       The nickname assigned to the profile.

   Methods
   -------
   to_dict()
       Converts the Profile object into a dictionary representation.
   """
    def __init__(self, profileId: int, userId: int, profileImage: int, nickname: str ):
        """
       Constructs all the necessary attributes for the Profile object.

       Parameters
       ----------
       profileId : int
           The unique identifier for the profile.
       userId : int
           The unique identifier of the user to whom this profile belongs.
       profileImage : int
           An identifier for the profile image associated with this profile.
       nickname : str
           The nickname assigned to the profile.
       """
        self.profileId = profileId
        self.userId = userId
        self.profileImage = profileImage
        self.nickname = nickname

    def to_dict(self):
        """
        Converts the Profile object into a dictionary representation.

        Returns
        -------
        dict
            A dictionary containing the attributes of the Profile object.
            {
                "profileId": int,
                "userId": int,
                "profileImage": int,
                "nickname": str
            }
        """
        return {
            "profileId" : self.profileId,
            "userId" : self.userId,
            "profileImage" : self.profileImage,
            "nickname" : self.nickname
        }
