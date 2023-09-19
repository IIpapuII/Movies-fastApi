from pydantic import BaseModel

class Movies(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str
     