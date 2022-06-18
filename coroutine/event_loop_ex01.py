import asyncio

async def func():
    await asyncio.sleep(0)
    return 999

loop = asyncio.get_event_loop()
coro = func()
print(loop.run_until_complete(coro))


# 이벤트루프를 얻는 2가지 방법
"""
추천 : asyncio.get_running_loop() >> 코루틴 내에서 호출 가능
비추천 : asyncio.get_event_loop() >> 어디서든 호출 가능
"""

loop1 = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()
print(loop1 is loop2)