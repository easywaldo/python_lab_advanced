import aiohttp
import asyncio

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response
loop = asyncio.get_event_loop()

coroutine = [get("http://example.com") for _ in range(8)]
results = loop.run_until_complete(asyncio.gather(*coroutine))

print("Results: %s" % results)
