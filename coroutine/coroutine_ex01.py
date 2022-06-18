async def func():
    return 123
print(type(func))

import inspect
print(inspect.iscoroutinefunction(func))


coro = func()   # 
print('====')
print(inspect.iscoroutine(coro))


try:
    coro.send(None)
except StopIteration as e:
    # 코루틴이 반환이 될때 실제로는 StopIteration 이 발생한다
    print('The answer was : ', e.value)
