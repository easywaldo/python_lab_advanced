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
patDataDict = {
    "name": "",
    "years_experience": 0,
    "address": ""
}


class PersonM:
    def __init__(self,
                  name: str,
                  years_experience: int,
                  address: str):
        self.name = name
        self.years_experience = years_experience
        self.address = address

pat_m = PersonM("Pat", 13, "123 Fake St.")