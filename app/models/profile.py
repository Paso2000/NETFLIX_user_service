class Profile:

    def __init__(self, profileId: int, userId: int, profileImage: int, nickname: str ):
        self.profileId = profileId
        self.userId = userId
        self.profileImage = profileImage
        self.nickname = nickname

    def to_dict(self):
        return {
            "profileId" : self.profileId,
            "userId" : self.userId,
            "profileImage" : self.profileImage,
            "nickname" : self.nickname
        }
