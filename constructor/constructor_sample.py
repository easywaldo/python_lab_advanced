from dataclasses import dataclass

class Person:
    name: str = ""
    years_experience: int = 0
    address: str = ""
    
pat = Person()
pat.name = "Pat"
print(f"Hello {pat.name}")


@dataclass
class PersonData():
    name: str = ""
    years_experience: int = 0
    address: str = ""
    
patData = PersonData("Pat", 13, "123 Fake St.")
patData = {
    "name": "",
    "years_experience": 0,
    "address": ""
}