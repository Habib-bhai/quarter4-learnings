from pydantic import BaseModel

# example of simple pydantic model
class Product(BaseModel):
    product_id: int
    product_name: str
    product_price: float
    product_description: str
    
    
# validating data with the model
product = {
    "product_id": 101,
    "product_name": "Laptop",
    "product_price": 1500.00,
    "product_description": "A high-performance laptop for gaming and work."
} 


product1 = Product(**product)

print(product1.model_dump())