import asyncio

# async def hello_world():
#     print("hello world")
#     return 42

# hello_world_coroutine = hello_world()

# print(hello_world_coroutine)

# event_loop = asyncio.get_event_loop()
# try:
#     print("entering event loop")
#     result = event_loop.run_until_complete(hello_world_coroutine)
#     print(result)
# finally:
#     event_loop.close()
    
    
async def add_42(number):
    print("Adding 42")
    return 42 + number

async def hello_world_s():
    print("hello world async def")
    result = await add_42(23)
    return result

event_loop_s = asyncio.get_event_loop()
try:
    result = event_loop_s.run_until_complete(hello_world_s())
    print(result)
finally:
    event_loop_s.close()
