class UpperCaseDict(dict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)
        
numbers = UpperCaseDict()
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3


from collections import UserDict
class NutritionalInformation(UserDict):
    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            pass
        for alias in get_aliases(key):
            try:
                return self.data[alias]
            except KeyError:
                pass
        raise KeyError(f"Could not find {key} or any of its aliases")

def get_aliases(alias: str) -> list[str]:
    aliases = {
        "rocket": "arugula",
        "jumbo": "orange",    
    }
    
    return list(aliases.values())

if __name__ == "__main__":
    print(numbers)
    nutrition = NutritionalInformation()
    nutrition["arugula"] = ["alpha", "beta", "delta"]
    print(nutrition)
    result = nutrition.get("rocket", "No Ingredient Found")
    print(result)
    