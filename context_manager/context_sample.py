class PizzaSpecification:
    def __init__(self, dough_radius_in_inches: int, toppings: list[str]):
        self.dough_radius_in_inches = dough_radius_in_inches
        self.toppings = toppings
        
def is_sauce(sauce: str):
    return True

import contextlib

@contextlib.contextmanager
def create_pizza_specification(dough_radius_in_inches: int,
                               toppings: list[str]):
        pizza_spec = PizzaSpecification(dough_radius_in_inches, toppings)
        yield pizza_spec
        assert 6<= pizza_spec.dough_radius_in_inches <= 12
        sauces = [t for t in pizza_spec.toppings if is_sauce(t)]
        assert len(sauces) < 2
        if sauces:
            assert pizza_spec.toppings[0] == sauces[0]
            
def test_pizza_options():
    with create_pizza_specification(8, ["Tomato Sauce", "Peppers"]) as pizza_spec:
        print('do something')

        
    

test_pizza_options()