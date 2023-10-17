from typing import Optional, List
from pydantic import BaseModel


class Amount(BaseModel):
    amount: float
    unit: str


class Ingredient(BaseModel):
    name: str
    amount: Optional[Amount]


class Recipe(BaseModel):
    title: str
    ingredients: List[Ingredient]
    description: str
