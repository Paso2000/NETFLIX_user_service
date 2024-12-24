# NETFILX_user_service
ASEE Project, content service part.

## ENTITY CLASSES
### User class
- userID : integer
- nome: String
- surname: String
- password: String
- email: String
- dateOfBirthday: Date
- paymentMethod: String
- profiles : array di profileId

## Profile class
- profileId : integer
- userId : integer
- profileImage : integer
- nickname : String
- recommendedList : array di filmId
- preferredList : array di filmId

### User service
- /users
    - GET
    - POST
- /users/{userId}
    - GET
    - PUT
    - DELETE
- /users/{userId}/profiles
    - GET
    - POST
- /users/{userId}/profiles/profile{id}
    - GET
    - PUT
    - DELETE


## Overview
