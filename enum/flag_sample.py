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


allergens = Allergen.FISH | Allergen.SHELLFISH
print(allergens)

if allergens & Allergen.FISH:
    print("This recipe contains fish.")
    
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
    
from fraction import Fraction
fraction_value = Fraction(numerator=3, denominator=5)
print(fraction_value)

