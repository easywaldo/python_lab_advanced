import collections
class AliasedIngredients(collections.abc.Set):
    def __init__(self, ingredients: set[str]):
        self.ingredients = ingredients
        
    def __contains__(self, value: str):
        return value in self.ingredients or \
            any(alias in self.ingredients for alias in get_aliases(value))
    
    def __iter__(self):
        return iter(self.ingredients)
    
    def __len__(self):
        return len(self.ingredients)


def get_aliases(alias: str) -> list[str]:
    aliases = {
        'rocket': 'arugula',
        'jumbo': 'orange',    
    }
    return list(aliases.values())


def print_items(items):
    for item in items:
        print(item)


if __name__ == "__main__":
    ingredients = AliasedIngredients({'arugula', 'eggplant', 'pepper'})

    for item in ingredients:
        print(item)

    print(len(ingredients))

    print('arugula' in ingredients)
    print('rocket' in ingredients)
    print(list(ingredients | AliasedIngredients({'garlic'})))
    
    
    
    print_items([1,2,3])
    print_items({4, 5, 6})
    print_items({"A": 1, "B": 2, "C": 3})
