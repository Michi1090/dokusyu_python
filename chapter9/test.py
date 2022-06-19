# 2
from time import time, sleep
from datetime import datetime

def time_deco(func):
    def inner(*args, **keywds):
        print(f'{func.__name__} Start: {datetime.fromtimestamp(time())}')
        result = func(*args, **keywds)
        print(f'{func.__name__} End: {datetime.fromtimestamp(time())}')
        return result
    return inner

@time_deco
def hoge():
    sleep(3)
    print('hoge is running')

hoge()

# 3
import asyncio
import time

async def heavy_process(name, sec):
    print(f'start {name}')
    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'start {name}/{sec}'

start = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
    asyncio.gather(
        heavy_process('hoge', 2),
        heavy_process('bar', 5),
        heavy_process('piyo', 1),
        heavy_process('spam', 3)
    )
)
end = time.time()
print(result)
print(f'Process Time: {end - start}')
