from pydantic import BaseModel,Field
from typing import Optional
class Movies(BaseModel):
    
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length= 15)
    overview: str = Field(min_length= 15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(default= 10, ge=1, le=10)
    category: str = Field(defautl="Categoría",min_length=5, max_length= 15)

    class Config:
        json_schema_extra = {
            "example":{
                "id": 1,
                "title": "Mi pelicua",
                "overview": "Descipcion de la pelea",
                "year": 2022,
                "rating": 9.5,
                "category": "Acción"
            }
        }     

class User(BaseModel):
    email:str
    password: str
