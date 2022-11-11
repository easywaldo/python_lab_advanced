from dataclasses import dataclass
import decimal
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


@dataclass(frozen=True)
class Item:
    name: str
    brand: str
    measure: ImperialMeasure
    price_in_cents: decimal.Decimal
    amount: float
    
test_item = Item(
    name="test",
    brand="test_brand",
    measure=ImperialMeasure.CUP,
    price_in_cents=10.5,
    amount=9.8
)

print(test_item)