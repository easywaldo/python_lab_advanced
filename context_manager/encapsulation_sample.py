def is_sauce():
    return True

class PizzaSpecification:
    def __init__(self, dough_radius_in_inches: int, toppings: list[str]):
        assert 6 <= dough_radius_in_inches < 12, \
            'Dough must be between 6 and 12 inches'
        self.__dough_radius_in_inches = dough_radius_in_inches
        self.__toppings: list[str] =list()
        self.__name = "test"

    def add_toppings(self, topping: str):
        '''
        Add a topping to the pizza
        All rules for pizza construction (one sauce, no sauce above
        cheese, etc.) still apply.
        '''
        if is_sauce(topping):
            self.__toppings.insert(0, topping)
        else:
            self.__toppings.append(topping)
            
    @property
    def dough_radius_in_inches(self):
        return self.__dough_radius_in_inches
            

pizza = PizzaSpecification(dough_radius_in_inches=11, toppings=["a", "b", "c"])
print(pizza.dough_radius_in_inches)