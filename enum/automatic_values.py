from enum import auto, Enum
from typing import Literal
class MotherSauce(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.capitalize()
    
    BÉCHAMEL = auto()
    VELOUTÉ = auto()
    ESPAGNOLE = auto()
    TOMATO = auto()
    HOLLANDAISE = auto()
    
print(list(MotherSauce))

sauce: Literal['Béchamel', 'Velouté', 'Espagnole',
               'Tomato', 'Hollandaise'] = 'Hollandaise'

print(sauce)

sauce: MotherSauce = MotherSauce.HOLLANDAISE
print(sauce)
