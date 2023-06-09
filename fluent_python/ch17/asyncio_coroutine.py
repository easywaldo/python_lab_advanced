import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine resumed")
    
async def main():
    print("Main started")
    await my_coroutine()
    print("Main completed")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

