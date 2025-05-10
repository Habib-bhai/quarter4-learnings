from pydantic import BaseModel
from typing import List, Optional


# class account(BaseModel):
#     account_id: int
#     bank_name: str


# class account_holder(BaseModel):
#     name: str
#     bank_and_account : account


# user_account = account(
#     account_id = 9292929229,
#     bank_name = "habib bank ltd"
# )



# user_account_holder = account_holder(
#     name= "habib",
#     bank_and_account  = user_account
# )


# print(user_account_holder)



class Lesson(BaseModel):
    topic: str
    length: int
    description: str
    

class Module(BaseModel):
    module_name: str
    lesson: Lesson
    

class Course(BaseModel):
    course_title: str
    course_duration: int
    course_price: float
    course_modules: Module 
    
       