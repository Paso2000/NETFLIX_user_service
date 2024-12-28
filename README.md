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


## POST Example
{
"userId": 1,
"name": "Mario",
"surname": "Rossi",
"password": "ciao",
"email": "mario@gmail.com",
"date_of_birth":  "05-03-1998",
"paymentMethod": "paypal",
"profiles": "1"
}

{
"profileId": 1, 
"userId": 1
"profileImage": 0,  
"nickname": "Default Profile"
}