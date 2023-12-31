from asyncio import sleep as asleep
def usage():
    rf, rt, sf, st = 0, 0, 0, 0
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'MemTotal' in line:
                rt = int(line.split()[1])
            elif 'MemFree' in line:
                rf = int(line.split()[1])
            elif 'SwapTotal' in line:
                st = int(line.split()[1])
            elif 'SwapFree' in line:
                sf = int(line.split()[1])
        if st == 0: # swap disabled
            st = 1
    return 1 - rf/rt, 1 - sf/st

async def co(MTAB={}):
    print("started mem")
    while True:
        ram,swap = usage()
        MTAB['mem'] = ram * 100
        MTAB['mem_level'] = ram * 5
        await asleep(1)
