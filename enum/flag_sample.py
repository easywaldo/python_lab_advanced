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