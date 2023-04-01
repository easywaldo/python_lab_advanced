from typing import Protocol, runtime_checkable, Any
from typing import Iterable, TYPE_CHECKING

@runtime_checkable
class RandomPicker(Protocol):
    _items: Iterable
    def __init__(self, items: Iterable):
        self._items = items
        
    def pick(self) -> Any:
        pass
    
import random


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


@runtime_checkable
class LoadableRandomPicker(RandomPicker, Protocol):
    def load(sel, Iterable) -> None:
        pass
    
loadable_random_picker = LoadableRandomPicker([1,2,3,])
print(isinstance(loadable_random_picker, LoadableRandomPicker))
print(isinstance(loadable_random_picker, SimplePicker))
print(isinstance(loadable_random_picker, RandomPicker))