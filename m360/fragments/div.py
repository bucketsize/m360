from time import strftime
from asyncio import sleep as asleep

async def co(MTAB={}):
    print("started div")
    s0, z0, c = 0, 0, 0
    while True:
        await asleep(3)
        x = 22/0
        await asleep(1)
