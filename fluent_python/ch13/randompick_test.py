from typing import Protocol, runtime_checkable, Any

@runtime_checkable
class RandomPicker(Protocol):
    def pick(self) -> Any:
        pass
    
import random
from typing import Iterable, TYPE_CHECKING


class SimplePicker:
    def __init__(self, items: Iterable) -> None:
        self._items = list(items)
        random.shuffle(self._items)
        
    def pick(self) -> Any:
        return self._items.pop()


def test_isinstance() -> None:
    popper: RandomPicker = SimplePicker([1])
    assert isinstance(popper, RandomPicker)
    print('success')
    
def test_item_type() -> None:
    items = [1, 2, 3, 4, 5]
    popper = SimplePicker(items)
    item = popper.pick()
    assert item in items
    if TYPE_CHECKING:
        reveal_type(item)   # randompick_test.py:24: note: Revealed type is 'Any'
    assert isinstance(item, int)
    print('success')


test_isinstance()
test_item_type()