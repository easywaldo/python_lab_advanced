from typing import TypeVar, Generic

class Beverage:
    """Any beverage."""
    
class Juice(Beverage):
    """Any fruit juice."""
    
class OrangeJuice(Juice):
    """Delicious juice from Brazilian oranges."""

T_co = TypeVar('T_co', covariant=True)

class BeverageDispenserCo(Generic[T_co]):
    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage
    
    def dispense(self) -> T_co:
        return self.beverage
    
def install_co(dispenser: BeverageDispenserCo[Juice]) -> None:
    """Install a fruit juice dispense."""
    
    
juice_dispenser = BeverageDispenserCo(Juice())
install_co(juice_dispenser)

orange_juice_dispenser = BeverageDispenserCo(OrangeJuice())
install_co(orange_juice_dispenser)