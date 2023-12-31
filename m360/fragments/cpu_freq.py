from os.path import isfile
from asyncio import sleep as asleep

cpufreq_files = []
for cpu in range(0, 127):
    cpuf = "/sys/devices/system/cpu/cpu%s/cpufreq/scaling_cur_freq" % cpu
    if isfile(cpuf):
        cpufreq_files.append(cpuf)

def usage():
    freq = []
    for file in cpufreq_files:
        with open(file, "r") as handle:
            result = handle.readline().strip()
            freq.append(int(result)/1000) # -> MHz
    return freq

async def co(MTAB={}):
    print("started cpu_freq")
    while True:
        freq = usage()
        sfreq, s = 0, 1
        for i, v in enumerate(freq):
            MTAB[f'{i}:cpu_freq'] = v
            sfreq += v
            s = i
        MTAB["m:cpu_freq"] = sfreq/s
        await asleep(1)
