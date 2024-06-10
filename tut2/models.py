from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    users = {
    "1": {
        "name": "John",
        "age": 20
    },
    "2": {
        "name": "Jane",
        "age": 21
    }
}
