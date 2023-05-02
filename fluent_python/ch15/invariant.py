from typing import TypeVar, Generic

class Beverage:
    """Any beverage."""
    
class Juice(Beverage):
    """Any fruit juice."""
    
class OrangeJuice(Juice):
    """Delicious juice from Brazilian oranges."""
    
T = TypeVar('T')

class BeverageDispenser(Generic[T]):
    """A dispenseer parameterized on the beverage type."""
    
    def __init__(self, beverage: T) -> None:
        self.beverage = beverage
        
    def dispense(self) -> T:
        return self.beverage
    

def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Install a fruit dispenser"""
    
juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser) # mypy error: Argument 1 to "install" has incompatible type "BeverageDispenser[Beverage]"; expected "BeverageDispenser[Juice]"

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser) # error: Argument 1 to "install" has incompatible type "BeverageDispenser[OrangeJuice]"; expected "BeverageDispenser[Juice]"