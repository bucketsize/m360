from os import getenv
from io import open
from time import strftime
from m360.config.sym import ascii as sym
from m360.config.formats import formatvalue 
from asyncio import sleep as asleep

async def co(mtab: {}):
    user = getenv("USER")
    sk = list(mtab.keys())
    sk.sort()
    with open("/var/tmp/m360.csv.out." + user, "w") as hout:
        while True:
            hout.write("{")
            for k in sk:
                hout.write(f"{k}={mtab[k]},")
            hout.write("}\n")
            hout.flush()
            await asleep(1) 
