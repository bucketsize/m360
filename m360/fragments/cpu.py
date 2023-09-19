from time import strftime
from asyncio import sleep as asleep

def usage():
    with open("/proc/stat", "r") as handle:
        result = handle.readline()
    t, s1, z1, i = [], 0, 0, 0
    for d in result.split()[1:]:
        s1 += int(d)
        t.append(d)
        i += 1
    z1 = t[3]
    return s1, z1

async def co(MTAB={}):
    s0, z0, c = 0, 0, 0
    while True:
        s, z = usage()
        c = 1 - (int(z) - int(z0)) / (int(s) - int(s0))
        s0, z0 = s, z
        MTAB['cpu'] = c * 100
        MTAB['cpu_level'] = c * 5
        MTAB['time'] = strftime("%Y-%m-%dT%H:%M:%S+05:30")
        # alert.check('cpu', c * 100)
        await asleep(1)
