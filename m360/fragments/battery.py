from asyncio import sleep as asleep
def usage():
    try:
        with open("/sys/class/power_supply/BAT0/capacity") as f:
            cap = f.read().strip()
    except:
            cap = "0"
    try:
        with open("/sys/class/power_supply/BAT0/status") as g:
            status = g.read().strip()
    except:
            status = "AC"
    return int(cap), status

async def co(MTAB={}):
    while True:
        level, status = usage()
        MTAB['battery_status'] = status
        MTAB['battery'] = level
        await asleep(1)
