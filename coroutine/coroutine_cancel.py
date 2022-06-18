import asyncio
async def func():
    try:
        while True: await asyncio.sleep(0)
    except asyncio.CancelledError:
        print('I was cancelled !!!')
    else:
        return 111

coro = func()
coro.send(None)
coro.send(None)
coro.throw(asyncio.CancelledError)