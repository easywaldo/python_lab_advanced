from dataclasses import dataclass
from enum import auto, Enum

class ImperialMeasure(Enum):
    CUP = auto()
    

@dataclass(frozen=True)
class Ingredient:
    name: str
    brand: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP
    

@dataclass
class Recipe:
    name: str
    ingredients: list[Ingredient]
    servings: int
    

test_ingredients = Ingredient(
    name="test_name",
    brand="test brand",
    amount=1,
    units=ImperialMeasure.CUP
)

print(test_ingredients)