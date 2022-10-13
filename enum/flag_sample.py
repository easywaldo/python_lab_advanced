from copy import deepcopy
from dataclasses import dataclass
import datetime
from enum import Enum, Flag, IntEnum, auto, unique
from typing import Set

class Allergen(Flag):
    FISH = auto()
    SHELLFISH = auto()
    TREE_NUTS = auto()
    PEANUTS = auto()
    GLUTEN = auto()
    SOY = auto()
    DAIRY = auto()
    SEAFOOD = FISH | SHELLFISH
    ALL_NUTS = TREE_NUTS | PEANUTS
    
allergens: Set[Allergen] = {Allergen.FISH, Allergen.SOY}

print(allergens)


# allergens = Allergen.FISH | Allergen.SHELLFISH
# print(allergens)

# if allergens & Allergen.FISH:
#     print("This recipe contains fish.")
    
print(Allergen.FISH in Allergen.SEAFOOD)
print(Allergen.FISH in Allergen.ALL_NUTS)

class ImperialLiquidMeasure(IntEnum):
    CUP = 8
    PINT = 16
    QUART = 32
    GALLON = 128

print("Compare IntEnum =================================================")
print(ImperialLiquidMeasure.CUP.value == 8)
print(ImperialLiquidMeasure.CUP.value)
assert(ImperialLiquidMeasure.CUP == 8)


class Kitchenware(IntEnum):
    PLATE = 7
    CUP = 8
    UTENSILS = 9
    
def pour_liquid(volume: ImperialLiquidMeasure):
    if volume == Kitchenware.CUP:
        print("same")
    else:
        print("different")
        
pour_liquid(ImperialLiquidMeasure.CUP)


@unique
class MotherSauce(Enum):
    BÉCHAMEL = "Béchamel"
    VELOUTÉ = "Velouté"
    ESPAGNOLE = "Espagnole"
    TOMATO = "Tomato"
    HOLLANDAISE = "Hollandaise"
    
# from fraction import Fraction
# fraction_value = Fraction(numerator=3, denominator=5)
# print(fraction_value)

@dataclass
class MyFraction:
    numerator: int = 2
    denominator: int = 3
    
MyFraction(numerator = 2, denominator = 3)


class ImperialMeasure(Enum):
    TEASPOON = auto()
    TABLESPOON = auto()
    CUP = auto()

class Broth(Enum):
    VEGETABLE = auto()
    CHICKEN = auto()
    BEEF = auto()
    FISH = auto()
    
@dataclass(frozen=True) 
# Ingredients added into the broth
class Ingredient:
    name: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP


@dataclass
class Recipe:
    aromatics: set[Ingredient]
    broth: Broth
    vegetables: set[Ingredient]
    meats: set[Ingredient]
    starches: set[Ingredient]
    garnishes: set[Ingredient]
    time_to_cook: datetime.timedelta
    
    def make_vegetarian(self):
        self.meats.clear()
        self.broth = Broth.VEGETABLE
        
    def get_ingredient_names(self):
        ingredients = (self.aromatics |
                       self.vegetables |
                       self.meats |
                       self.starches |
                       self.garnishes)
        return ({i.name for i in ingredients} | {self.broth.name.capitalize() + " broth"})
    
    
pepper = Ingredient("Pepper", 1, ImperialMeasure.TABLESPOON)
garlic = Ingredient("Garlic", 2, ImperialMeasure.TEASPOON)
carrots = Ingredient("Carrots", .25, ImperialMeasure.CUP)
celery = Ingredient("Celery", .25, ImperialMeasure.CUP)
onions = Ingredient("Onions", .25, ImperialMeasure.CUP)
parsley = Ingredient("Parsley", 2, ImperialMeasure.TABLESPOON)
noodles = Ingredient("Noodles", 1.5, ImperialMeasure.CUP)
chicken = Ingredient("Chicken", 1.5, ImperialMeasure.CUP)

chicken_noodle_soup = Recipe(
    aromatics={pepper, garlic},
    broth=Broth.CHICKEN,
    vegetables={celery, onions, carrots},
    meats={chicken},
    starches={noodles},
    garnishes={parsley},
    time_to_cook=datetime.timedelta(minutes=60))

# incorrect_ingredients = Ingredient(name="good", amount=100, units="Unknown")

print(chicken_noodle_soup.broth)
chicken_noodle_soup.garnishes.add(pepper)
print(chicken_noodle_soup.garnishes)

noodle_soup = deepcopy(chicken_noodle_soup)
noodle_soup.make_vegetarian()
print(noodle_soup.get_ingredient_names())

print(str(chicken_noodle_soup))

print(chicken_noodle_soup == noodle_soup)
print(noodle_soup == deepcopy(noodle_soup))


from typing import TypedDict
class Range(TypedDict):
    min: float
    max: float
    
@dataclass(eq=True, frozen=True)
class NutritionInformation:
    calories: int
    fat: int
    carbohydrates: int
    
    def __lt__(self, rhs) -> bool:
        return ((self.fat, self.carbohydrates, self.calories) <
                (rhs.fat, rhs.carbohydrates, rhs.calories))

    def __le__(self, rhs) -> bool:
        return self < rhs or self == rhs

    def __gt__(self, rhs) -> bool:
        return not self <= rhs

    def __ge__(self, rhs) -> bool:
        return not self < rhs
    

nutritionals = [NutritionInformation(calories=100, fat=1, carbohydrates=3),
                NutritionInformation(calories=50, fat=6, carbohydrates=4),
                NutritionInformation(calories=125, fat=12, carbohydrates=3)]

print("sorted")
print(sorted(nutritionals))
    # TypeError: '<' not supported between instances of
    # 'NutritionInformation' and 'NutritionInformation'
    #
    
n1 = NutritionInformation(calories=200, fat=1, carbohydrates=3)
n1.calories = 100