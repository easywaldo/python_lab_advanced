from collections.abc import Generator
from typing import TypeAlias, Union, NamedTuple

class Result(NamedTuple):
    count: int
    average: float
    
class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'
    
STOP = Sentinel()
SendType: TypeAlias = float | Sentinel

def averager2(verbose: bool = False) -> Generator[None, float | Sentinel, Result]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        if verbose:
            print('received:', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(total, average)


coro_avg = averager2()
next(coro_avg)

result = coro_avg.send(10)
print(result)

result = coro_avg.send(30)
print(result)

result = coro_avg.send(6.5)
print(result)

coro_avg.close()