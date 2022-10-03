# def reverse(coll: list) -> list:
#     return coll[::-1]

from typing import TypeVar, Generic
T = TypeVar('T', float, int, contravariant=False)
def reverse(coll: Generic[T]) -> Generic[T]:
    return coll[::-1]

def repeat(coll: Generic[T], num: int)-> Generic[T]:
    return [coll]*num

list_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
print(reverse(list_numbers))

S = TypeVar('S', str, bytes)
def reverse_str(coll: S) -> S:
    return coll[::-1]

print(reverse_str("helloworld"))
print(reverse_str([1,2,3,]))

