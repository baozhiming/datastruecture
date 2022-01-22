import threading
import asyncio


async def hello1():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = await asyncio.sleep(3)
    print("Hello again!")
loop = asyncio.get_event_loop()
loop.run_until_complete(hello1())
loop.close()
