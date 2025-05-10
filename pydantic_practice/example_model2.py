from pydantic import BaseModel # type: ignore

# example of nested models


class Engine(BaseModel):
    horsepower: int
    
class Car(BaseModel):
    car_color :  str
    car_model: str
    car_speed: int
    car_engine: Engine 
    
    
try:
    
    invalid_car = Car(car_color="red", car_model="Toyota", car_speed=200, car_engine={"horsepower": "fast"})
    
except ValueError as e:
    
    print(f"Validation error: {e}")
    
           