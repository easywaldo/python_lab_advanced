from enum import Flag, auto
from typing import Set

class Allergen(Flag):
    FISH = auto()
    SHELLFISH = auto()
    TREE_NUTS = auto()
    PEANUTS = auto()
    GLUTEN = auto()
    SOY = auto()
    DAIRY = auto()
    
allergens: Set[Allergen] = {Allergen.FISH, Allergen.SOY}

print(allergens)


allergens = Allergen.FISH | Allergen.SHELLFISH
print(allergens)

if allergens & Allergen.FISH:
    print("This recipe contains fish.")