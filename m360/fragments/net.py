from subprocess import check_output
from re import search
from time import process_time, sleep
from asyncio import sleep as asleep

net_stat_pat = r"(\w+:)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)"
wls_stat_pat = r"(\w+:)\s+(\d+)\s+(\d+).\s+(.\d+)."

def usage():
    default:str=""
    devices:[(str,int,int)]=[]
    wireless: [(str,int,int,int)]=[]
    with open("/proc/net/dev", "r") as f:
        for l in f.readlines():
            m = search(net_stat_pat, l)
            if m:
                devices.append((m.group(1)[:-1],
                                int(m.group(2)),
                                0))
    with open("/proc/net/wireless", "r") as f:
        for l in f.readlines():
            m = search(wls_stat_pat, l)
            if m:
                wireless.append((m.group(1),
                            int(m.group(2)),
                            int(m.group(3)),
                            0))
    return default, devices, wireless

async def co(MTAB={}):
    tx0, rx0, devc = 0, 0, ""
    while True:
        defdev, devices, wireless = usage()
        for i, j in enumerate(devices):
            ix = str(i)
            dev, tx, rx = j
            ts, rs = (tx-tx0)/process_time(), (rx-rx0)/process_time()
            tx0, rx0 = tx, rx
            if ts > 0:
                devc = dev
            MTAB[ix+':net_device'] = dev
            MTAB[ix+':net_tx'] = tx/100
            MTAB[ix+':net_rx'] = rx/100
            MTAB[ix+':net_ts'] = ts/100
            MTAB[ix+':net_rs'] = rs/100
        MTAB['net_gateway'] = devc
        await asleep(1)

if __name__ == '__main__':
    m={}
    for i in co_usage(m):
        print(m)
        sleep(1)
