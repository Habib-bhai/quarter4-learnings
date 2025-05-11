from fastapi import FastAPI, Path , Query# type: ignore
from typing import Optional

app = FastAPI()

# path parameters --> when there is a variable in the path


# when there is path parameter we will use the fastapi's built in "Path" utility to validate that particular path parameter
@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(
        ...,
        title = "The id of the item",
        description = "The id of the item to read",
        gt = 0,
    ),
    price: Optional[int] = None):
    return {"item_id": item_id, "price": price}




# when you have to validate a query i.e. things written after a "?" mark in a url.
# we are going to use "Query" of fastapi to validate that.
@app.get("/blog")
def read_blog(
    search_term: str = Query(..., max_length=200, min_length=3)
):
    if search_term:
        return f"Search term: {search_term}, FOUND!!!"


    
# if by mistake, or for experimenting, I use "Path" to validate, query parameters, fastapi won't be able to find it.