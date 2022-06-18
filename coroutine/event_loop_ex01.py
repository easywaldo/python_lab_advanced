import asyncio

async def func():
    await asyncio.sleep(0)
    return 999

loop = asyncio.get_event_loop()
coro = func()
print(loop.run_until_complete(coro))