import os
import io
from time import strftime
from m360.config.sym import ascii as sym
from m360.config.formats import formatvalue 
from asyncio import sleep as asleep

mget = lambda m, k: m[k] if k in m else k
fget = lambda m, k: formatvalue(k, m[k]) if k in m else "?"

def statusline(mtab: {}) -> str:
    return "%%{l} %s%s %%{c}...%%{r} %s%s %s%s | %s%s | %s%s | %s%s | %s%s | %s%s\n" % (
        sym["clock"],
        strftime("%a %b %d, %Y | %H:%M:%S"),
        sym["cpu"],
        fget(mtab, "cpu"),
        sym["cpu_temp"],
        fget(mtab, "cpu_temp"),
        mget(sym,  mget(mtab, 'gpu_id')+":gpu"),
        fget(mtab, mget(mtab, 'gpu_id')+":gpu_temp"),
        sym["mem"],
        fget(mtab, "mem"),
        sym["audio"],
        fget(mtab, "vol"),
        sym["net"],
        fget(mtab, "net_gateway"),
        mget(sym, "bat_"+fget(mtab, "battery_status").lower()),
        fget(mtab, "battery"),
    )

async def co(mtab: {}):
    user = os.getenv("USER")
    with io.open("/tmp/m360.lemonbar.out." + user, "w") as hout:
        while True:
            hout.write(statusline(mtab))
            hout.flush()
            await asleep(1) 
