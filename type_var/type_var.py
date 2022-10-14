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


import logging
from typing import TypeVar, Generic
from logging import NOTSET, Logger, getLogger
T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)
        
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
logger_ex = getLogger(name="easywaldo")
logger = LoggedVar(
    value=str, 
    name="easywaldo", 
    logger=logger_ex)
logger.log("hello my world")
logging.info("hello world")


