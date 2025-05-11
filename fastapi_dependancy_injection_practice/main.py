from fastapi import FastAPI, Depends,HTTPException #type: ignore
from typing import Annotated
from starlette import status

app = FastAPI()

def hello_world_dependancy():
    return f"HELLO FROM DEPENDANCY WORLD"

# simple dependancy injection
@app.get("/hello")
def hello(hello_world: str = Depends(hello_world_dependancy)):
    return hello_world


# dependancy injection that requires parameters
# if we provide a simple dependancy like below.
# it is expected to come from the "query parameters"
# or it can be extracted from maybe Headers, Cookies etc
def get_user(user_id: str):
    # fetched user from db.
    return {"user_id": user_id, "name": f"John Doe {user_id}"}


@app.get("/user")
def path_operation_functino(user: dict = Depends(get_user)):
    return user



# Multiple dependency example

@app.get("/multiple")
def multiple_dependancy(user: Annotated[dict,Depends(get_user)], hello_world : Annotated[str,Depends(hello_world_dependancy)]):
    return {"user": user, "": hello_world}


# class dependency

blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

class GetObjectOr404():
    def __init__(self, model)->None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

