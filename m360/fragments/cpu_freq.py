import os

cpufreq_files = []
for cpu in range(0, 127):
    cpuf = "/sys/devices/system/cpu/cpu%s/cpufreq/scaling_cur_freq" % cpu
    if os.path.isfile(cpuf):
        cpufreq_files.append(cpuf)

def usage():
    freq = []
    for file in cpufreq_files:
        with open(file, "r") as handle:
            result = handle.readline().strip()
            freq.append(int(result)/1000) # -> MHz
    return freq

def co_usage(MTAB={}):
    while True:
        freq = usage()
        sfreq, s = 0, 0
        for i, v in enumerate(freq):
            MTAB[str(i-1)+':cpu_freq'] = v
            sfreq += v
            s = i
        MTAB["m:cpu_freq"] = sfreq/s
        yield
