from pydantic import BaseModel,  EmailStr, validator, pydantic  # type: ignore
from typing import List


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]    

    @validator("name")
    def name_must_be_habib(cls, value):
        if value == "habib":
            print("VERY GOOD YOU ARE HABIB 😁")
        else:
            raise     
    