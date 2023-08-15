from subprocess import check_output
from re import search
from time import process_time

def usage():
    try:
        output = check_output(["ip", "route"]).decode()
        match = search(r"default via (\d+\.\d+\.\d+\.\d+) dev (\w+)", output)
        if match is None:
            return "?", "?", "?", 0, 0
        net_stat_pat = match.group(2) + ": (.+)\n"
        with open("/proc/net/dev", "r") as f:
            r2 = f.read()
        r3 = search(net_stat_pat, r2).group(1)
        t = [int(i) for i in r3.split()]
        return match.group(1), match.group(2), "?", t[0], t[8]
    except:
        return "?", "?", "?", 0, 0

def co_usage(MTAB={}):
    tx0, rx0 = 0, 0
    while True:
        gw, dev, proto, tx, rx = usage()
        ts, rs = (tx-tx0)/process_time(), (rx-rx0)/process_time()
        tx0, rx0 = tx, rx
        MTAB['net_gateway'] = gw
        MTAB['net_device'] = dev
        MTAB['net_proto'] = proto
        MTAB['net_tx'] = tx/100
        MTAB['net_rx'] = rx/100
        MTAB['net_ts'] = ts/100
        MTAB['net_rs'] = rs/100
        yield
